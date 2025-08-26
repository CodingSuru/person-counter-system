import cv2
import json
import os
from datetime import datetime
from ultralytics import YOLO
import threading

class PersonCounter:
    def __init__(self):
        try:
            self.model = YOLO('yolo11n.pt')
        except Exception as e:
            print(f"YOLO model loading error: {e}")
            self.model = None
        self.max_person_count = 0
        self.current_count = 0
        self.data_file = 'backend/data.json'
        self.lock = threading.Lock()  # Add lock for thread-safe file operations
        
    def detect_people(self, frame):
        try:
            if self.model is None:
                return 0, []
            
            results = self.model(frame, verbose=False)
            boxes = []
            person_count = 0
            
            for result in results:
                for box in result.boxes:
                    if box.cls == 0:  # Class 0 is 'person' in COCO dataset
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        boxes.append([int(x1), int(y1), int(x2-x1), int(y2-y1)])
                        person_count += 1
            
            return person_count, boxes
        except Exception as e:
            print(f"Detection error: {e}")
            return 0, []
    
    def save_data(self, count, change_type, source):
        try:
            with self.lock:  # Ensure thread-safe file access
                data = []
                if os.path.exists(self.data_file):
                    try:
                        with open(self.data_file, 'r') as f:
                            content = f.read().strip()
                            if content:
                                data = json.loads(content)
                            else:
                                print(f"Warning: {self.data_file} is empty, initializing with empty list")
                                data = []
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from {self.data_file}: {e}. Initializing with empty list")
                        data = []
                    except Exception as e:
                        print(f"Error reading {self.data_file}: {e}. Initializing with empty list")
                        data = []
                
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                entry = {
                    'timestamp': timestamp,
                    'person_count': count,
                    'change_type': change_type,
                    'max_count': self.max_person_count,
                    'source': source
                }
                data.append(entry)
                
                # Keep only the last 200 entries
                if len(data) > 200:
                    data = data[-200:]
                
                with open(self.data_file, 'w') as f:
                    json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Save data error: {e}")
    
    def generate_frames(self, source, source_type):
        try:
            if source_type == 'file':
                cap = cv2.VideoCapture(source)
            elif source_type == 'android':
                # Optimized configuration for Android IP camera
                cap = cv2.VideoCapture(source)
                cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Minimal buffer for real-time
                cap.set(cv2.CAP_PROP_FPS, 15)  # Lower FPS for stability
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            else:
                cap = cv2.VideoCapture(source)
                
            if not cap.isOpened():
                print(f"Cannot open source: {source}")
                return
                
            frame_count = 0
            last_detection_result = (0, [])  # Cache last detection results
            detection_interval = 5 if source_type == 'android' else 1  # Process every 5th frame for Android
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    if source_type == 'file':
                        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        continue
                    else:
                        print(f"Failed to read frame from {source_type} source")
                        break
                
                frame_count += 1
                
                # Resize frame for consistent processing on Android
                if source_type == 'android':
                    frame = cv2.resize(frame, (640, 480))
                
                # Perform detection only on specific frames for Android
                if source_type == 'android' and frame_count % detection_interval == 0:
                    count, boxes = self.detect_people(frame)
                    last_detection_result = (count, boxes)
                    
                    # Update counts and save data only when detection runs
                    if count != self.current_count:
                        if count > self.current_count:
                            change_type = 'increase'
                        else:
                            change_type = 'decrease'
                        
                        self.current_count = count
                        if count > self.max_person_count:
                            self.max_person_count = count
                        
                        self.save_data(count, change_type, source_type)
                else:
                    # Use cached detection results for non-detection frames
                    if source_type == 'android':
                        count, boxes = last_detection_result
                    else:
                        count, boxes = self.detect_people(frame)
                        
                        # Update counts for non-Android sources
                        if count != self.current_count:
                            if count > self.current_count:
                                change_type = 'increase'
                            else:
                                change_type = 'decrease'
                            
                            self.current_count = count
                            if count > self.max_person_count:
                                self.max_person_count = count
                            
                            self.save_data(count, change_type, source_type)
                
                # Always draw bounding boxes and overlays for consistency
                for (x, y, w, h) in boxes:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, 'Person', (x, y-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                
                # Add consistent text overlay
                cv2.putText(frame, f'Current: {self.current_count}', (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f'Max: {self.max_person_count}', (10, 70), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                
                # Add source type indicator
                source_text = f'Source: {source_type.upper()}'
                if source_type == 'android':
                    detection_status = "DETECTING" if frame_count % detection_interval == 0 else "CACHED"
                    source_text += f' ({detection_status})'
                cv2.putText(frame, source_text, (10, 110), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                
                # Consistent JPEG encoding
                jpeg_quality = 75 if source_type == 'android' else 90
                ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])
                if ret:
                    frame_bytes = buffer.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
                           
        except Exception as e:
            print(f"Frame generation error: {e}")
        finally:
            try:
                cap.release()
            except:
                pass
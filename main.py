from flask import Flask, render_template, Response, request, jsonify
import cv2
import json
import os
from datetime import datetime
from maxperson import PersonCounter
import threading

app = Flask(__name__)
person_counter = PersonCounter()
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_video', methods=['POST'])
def upload_video():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        video_file = request.files['video']
        if video_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        if video_file and video_file.filename.endswith('.mp4'):
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
            video_file.save(video_path)
            return jsonify({'video_path': video_path})
        else:
            return jsonify({'error': 'Invalid file format. Please upload an MP4 file'}), 400
    except Exception as e:
        print(f"Error uploading video: {e}")
        return jsonify({'error': 'Server error during upload'}), 500

@app.route('/video_feed/<source>', methods=['GET', 'POST'])
def video_feed(source):
    try:
        if source == 'sample':
            video_path = request.args.get('video_path') or os.getenv('SAMPLE_VIDEO_PATH', 'sample/sample.mp4')
            if not os.path.exists(video_path):
                print(f"Video file not found: {video_path}")
                return "Video file not found", 404
            return Response(person_counter.generate_frames(video_path, 'file'),
                          mimetype='multipart/x-mixed-replace; boundary=frame')
        elif source == 'camera':
            camera_url = request.args.get('camera_url') or os.getenv('RTSP_CAMERA_URL', '')
            if not camera_url:
                return "Camera URL not provided", 400
            return Response(person_counter.generate_frames(camera_url, 'rtsp'),
                          mimetype='multipart/x-mixed-replace; boundary=frame')
        elif source == 'android':
            android_url = request.args.get('android_url') or os.getenv('ANDROID_CAMERA_URL', '')
            if not android_url:
                return "Android camera URL not provided", 400
            return Response(person_counter.generate_frames(android_url, 'android'),
                          mimetype='multipart/x-mixed-replace; boundary=frame')
        else:
            return "Invalid source", 400
    except Exception as e:
        print(f"Error in video feed: {e}")
        return "Video feed error", 500

@app.route('/get_data')
def get_data():
    try:
        if os.path.exists('backend/data.json'):
            with open('backend/data.json', 'r') as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
                    return jsonify(data)
        # Initialize empty JSON file if doesn't exist or is empty
        with open('backend/data.json', 'w') as f:
            json.dump([], f)
        return jsonify([])
    except Exception as e:
        print(f"Error getting data: {e}")
        # Create empty JSON file
        try:
            with open('backend/data.json', 'w') as f:
                json.dump([], f)
        except:
            pass
        return jsonify([])

if __name__ == '__main__':
    os.makedirs('backend', exist_ok=True)
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', 5000)), threaded=True)
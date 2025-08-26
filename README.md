Person Counter System 🚶‍♂️📹
Welcome to the Person Counter System! 🎉 This Flask-based web application uses the powerful YOLOv11 model to detect and count people in real-time video streams from various sources, including local MP4 files, RTSP cameras, and Android phone cameras. It tracks the current and maximum number of people detected, logs data in a JSON file (limited to 200 entries), and provides a user-friendly web interface with options to upload videos or use a pre-uploaded sample. 🖥️
🌟 Features

Real-Time Detection: Uses YOLOv11 to identify and count people in video streams with high accuracy. 🔍
Multiple Sources: Supports local MP4 files 📁, RTSP camera streams 📹, and Android phone cameras 📱.
Video Upload: Upload your own MP4 video or use a pre-uploaded sample video for person counting. 🎥
Interactive Web Interface: Displays live video feeds with bounding boxes, current/maximum counts, and recent activity logs. 📊
Secure Camera Access: Login interface for entering RTSP or Android camera URLs securely. 🔒
Data Management: Stores up to 200 detection records in data.json, overwriting older entries to keep things tidy. 📝
Responsive Design: Built with Tailwind CSS for a modern, mobile-friendly interface. 📱💻

📋 Prerequisites
To run this project, you’ll need:

Python 3.8+ 🐍
A compatible video source:
Local MP4 file (e.g., sample.mp4) or uploaded MP4 file 📁
RTSP camera with a valid URL (e.g., rtsp://username:password@host:port/path) 📹
Android phone with an IP Webcam app (e.g., http://host:port/videofeed) 📱


YOLOv11 Model File (yolo11n.pt) for person detection. 🧠
A modern web browser (Chrome, Firefox, etc.) 🌐

🛠️ Setup Instructions
Follow these steps to get the project up and running locally:

Clone the Repository 📥
git clone https://github.com/your-username/person-counter-system.git
cd person-counter-system


Install Dependencies 🛠️Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt

This installs Flask, OpenCV, Ultralytics (for YOLO), and NumPy.

Download YOLO Model 🧠

Download the yolo11n.pt model from the Ultralytics YOLOv11 repository or use a pre-trained model.
Place yolo11n.pt in the project root directory (person-counter-system/).


Prepare Video Sources 🎥

Local Video: Place a sample MP4 file in the sample/ directory (e.g., sample/sample.mp4) for the pre-uploaded option.
Uploaded Video: Use the web interface to upload your own MP4 video.
RTSP Camera: Obtain the RTSP URL for your camera (e.g., rtsp://username:password@host:port/path). You’ll enter this in the web interface.
Android Camera: Install an IP Webcam app (e.g., IP Webcam) on your Android phone, ensure it’s on the same network as your server, and note the URL (e.g., http://host:port/videofeed).


Run the Application 🚀Start the Flask server:
python main.py

Open your browser and navigate to http://localhost:5000 to access the web interface. 🌐


🌐 Usage

Select a Video Source 📡

On the homepage, choose a video source:
Sample Video (MP4) 📁: Opens a form to either upload a new MP4 video or use the pre-uploaded sample.mp4.
IP Camera Feed 📹: Prompts for an RTSP URL.
Android Phone Camera 📱: Prompts for an MJPEG URL.


For Sample Video, choose to upload a new video or use the pre-uploaded one. For IP Camera or Android Phone, enter the camera URL in the login form and click "Connect".


View the Feed 📺

The video feed displays with green bounding boxes around detected people.
Text overlays show the current person count (green), maximum count (red), and source type (yellow).


Monitor Data 📊

The interface shows:
Current Count: Number of people currently detected.
Maximum Count: Highest number of people detected in the session.
Total Records: Number of logged detection events (up to 200).
Recent Activity: A table of the last 5 detection events, including timestamp, person count, change type, and max count.





🚀 Deployment
To share your project with the world, deploy it to a hosting service like Render or Heroku. Here’s how:

Prepare the Repository 📦

Ensure all files are committed to your GitHub repository (excluding yolo11n.pt, sample.mp4, uploads/, and data.json as per .gitignore).
Push to GitHub:git add .
git commit -m "Ready for deployment"
git push origin main




Set Up on Render 🌍

Sign up at Render and create a new Web Service.
Link your GitHub repository and configure:
Build Command: pip install -r requirements.txt
Start Command: python main.py
Environment Variables (optional):
SAMPLE_VIDEO_PATH: Path to your sample video (e.g., sample/sample.mp4).
PORT: Server port (default: 5000).




Note: YOLO processing and video uploads are resource-intensive. A paid Render plan may be required for stable performance.


Provide Camera URLs 🔗

For RTSP or Android camera feeds, ensure the URLs are accessible from the deployed server (e.g., public IPs or same network).
Users will enter camera URLs or upload videos via the web interface.


Share the URL 🔗

Once deployed, Render provides a URL (e.g., https://your-app-name.onrender.com).
Share this link with others to showcase your person counting system! 🎉



📂 Project Structure
person-counter-system/
├── backend/                    # Stores detection data
│   └── data.json               # Logs up to 200 detection records
├── sample/                     # Sample video files
│   └── sample.mp4              # Example MP4 file (not in repo)
├── uploads/                    # Temporary storage for uploaded videos
├── templates/                  # HTML templates
│   └── index.html              # Web interface
├── .gitignore                  # Excludes sensitive/large files
├── main.py                     # Flask app entry point
├── maxperson.py                # Person detection logic
├── yolo11n.pt                  # YOLO model (not in repo)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

🛡️ Notes

YOLO Model: The yolo11n.pt file is large and excluded from the repository. Download it from Ultralytics and place it in the root directory.
Sample Video: Provide your own sample.mp4 in the sample/ directory, as it’s excluded from the repository.
Uploaded Videos: Uploaded videos are stored in the uploads/ directory, which is excluded from the repository.
Camera URLs: For RTSP or Android cameras, ensure URLs are valid and accessible. Embed credentials in the URL if needed (e.g., rtsp://username:password@host:port/path).
Data Limit: The data.json file stores only the most recent 200 detection records.
Performance: YOLO processing is CPU/GPU-intensive. Test thoroughly on your deployment platform to ensure stability.

🐛 Troubleshooting

Video Feed Not Loading:
Check if the video file or camera URL is correct and accessible from the server.
Ensure the server and camera are on the same network (for local testing) or use public IPs (for deployment).


Upload Errors:
Ensure the uploaded file is a valid MP4.
Check server storage permissions for the uploads/ directory.


YOLO Model Error:
Verify that yolo11n.pt is in the project root directory.
Ensure Ultralytics is installed (pip install ultralytics).


Slow Performance:
YOLO processing is resource-heavy. Use a server with sufficient CPU/GPU resources or optimize the detection interval in maxperson.py.


Deployment Issues:
Check Render/Heroku logs for errors.
Ensure all dependencies are listed in requirements.txt.



🤝 Contributing
Want to make this project even better? 🌟 Contributions are welcome!

Fork the repository.
Create a new branch (git checkout -b feature/awesome-feature).
Make your changes and commit (git commit -m "Add awesome feature").
Push to your branch (git push origin feature/awesome-feature).
Open a Pull Request on GitHub.

Please include a clear description of your changes and test them thoroughly. 🙌
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
🙏 Acknowledgments

Ultralytics for the YOLOv11 model.
Flask for the web framework.
OpenCV for video processing.
Tailwind CSS for responsive styling.

Happy counting! 🚶‍♀️🚶‍♂️
# Person Counter System 🚶‍♂️📹  

Welcome to the **Person Counter System**! 🎉  
This **Flask-based web application** uses the powerful **YOLOv11** model to detect and count people in **real-time video streams** from various sources, including local MP4 files, RTSP cameras, and Android phone cameras.  

It tracks the **current** and **maximum** number of people detected, logs data in a **JSON file (limited to 200 entries)**, and provides a **user-friendly web interface** with options to upload videos or use a pre-uploaded sample. 🖥️  

---

## 🌟 Features  

- **Real-Time Detection**: Uses YOLOv11 to identify and count people in video streams with high accuracy. 🔍  
- **Multiple Sources**: Supports local MP4 files 📁, RTSP camera streams 📹, and Android phone cameras 📱.  
- **Video Upload**: Upload your own MP4 video or use a pre-uploaded sample video for person counting. 🎥  
- **Interactive Web Interface**: Displays live video feeds with bounding boxes, current/maximum counts, source type, and recent activity logs. 📊  
- **Secure Camera Access**: Login interface for entering RTSP or Android camera URLs securely. 🔒  
- **Data Management**: Stores up to 200 detection records in `data.json`, including timestamp, person count, change type, max count, and source type. 📝  
- **Responsive Design**: Built with **Tailwind CSS** for a modern, mobile-friendly interface. 📱💻  

---

## 📋 Prerequisites  

To run this project, you’ll need:  

- Python **3.8+** 🐍  
- A compatible video source:  
  - Local MP4 file (e.g., `sample.mp4`) or uploaded MP4 file 📁  
  - RTSP camera with a valid URL (e.g., `rtsp://username:password@host:port/path`) 📹  
  - Android phone with an IP Webcam app (e.g., `http://host:port/videofeed`) 📱  
- **YOLOv11 Model File** (`yolo11n.pt`) for person detection. 🧠  
- A modern web browser (Chrome, Firefox, etc.) 🌐  

---

## 🛠️ Setup Instructions  

### 1. Clone the Repository 📥  
```bash
git clone https://github.com/your-username/person-counter-system.git
cd person-counter-system
```

### 2. Install Dependencies 🛠️  
```bash
pip install -r requirements.txt
```  
This installs **Flask, OpenCV, Ultralytics (YOLO), and NumPy**.  

### 3. Download YOLO Model 🧠  
- Download `yolo11n.pt` from the **Ultralytics YOLOv11 repository** or use a pre-trained model.  
- Place `yolo11n.pt` in the project **root directory** (`person-counter-system/`).  

### 4. Prepare Video Sources 🎥  
- **Local Video**: Place a sample MP4 file in the `sample/` directory (e.g., `sample/sample.mp4`).  
- **Uploaded Video**: Use the web interface to upload your own MP4 video.  
- **RTSP Camera**: Obtain the RTSP URL and enter it in the web interface.  
- **Android Camera**: Use an IP Webcam app and ensure the phone is on the same network.  

### 5. Run the Application 🚀  
```bash
python main.py
```  
Then open **http://localhost:5000** in your browser. 🌐  

---

## 🌐 Usage  

### Select a Video Source 📡  
- **Sample Video (MP4)** 📁  
- **IP Camera Feed** 📹  
- **Android Phone Camera** 📱  

Enter the **camera URL** in the login form when needed and click **Connect**.  

### View the Feed 📺  
- Green **bounding boxes** around detected people.  
- Text overlays show:  
  - Current Count ✅  
  - Maximum Count 🔴  
  - Source Type 🟨  

### Monitor Data 📊  
- **Current**: People detected right now.  
- **Max**: Highest count detected.  
- **Source**: FILE, RTSP, ANDROID.  
- **Recent Activity**: Table of last 5 detection events (with timestamp, person count, change type, max count, and source).  

---

## 🚀 Deployment  

### Prepare the Repository 📦  
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```  

### Deploy on Render 🌍  
- Build Command: `pip install -r requirements.txt`  
- Start Command: `python main.py`  
- Env Vars:  
  - `SAMPLE_VIDEO_PATH` = `sample/sample.mp4`  
  - `PORT` = 5000  

⚠️ Note: YOLO + video = resource heavy. Paid plan may be required.  

---

## 📂 Project Structure  

```
person-counter-system/
├── backend/          # Detection data
│   └── data.json     # Logs up to 200 records
├── sample/           # Sample videos
│   └── sample.mp4
├── uploads/          # Uploaded videos
├── templates/        # HTML
│   └── index.html
├── main.py           # Flask app
├── maxperson.py      # YOLO detection logic
├── requirements.txt  # Dependencies
└── README.md         # Docs
```

---

## 📊 Data Storage  

`data.json` stores detection records:  

```json
[
  {
    "timestamp": "2025-08-26 11:42:00",
    "person_count": 9,
    "change_type": "increase",
    "max_count": 9,
    "source": "file"
  }
]
```  

---

## 🛡️ Notes  

- **YOLO Model**: `yolo11n.pt` excluded from repo → download manually.  
- **Sample Video**: Place `sample.mp4` yourself.  
- **Uploads**: Stored in `uploads/`, excluded from repo.  
- **Data Limit**: Only last **200 records** saved.  
- **Performance**: Heavy on CPU/GPU, optimize for deployment.  

---

## 🐛 Troubleshooting  

- **Video Feed Not Loading** → Check video path / URL / network.  
- **Counts Not Updating** → Ensure `data.json` is being written.  
- **Upload Errors** → Only valid MP4 files allowed.  
- **YOLO Model Error** → Place `yolo11n.pt` in root.  
- **Slow Performance** → Use better hardware / reduce detection interval.  

---

## 🤝 Contributing  

1. Fork the repo  
2. Create branch → `git checkout -b feature/awesome-feature`  
3. Commit changes → `git commit -m "Add awesome feature"`  
4. Push branch → `git push origin feature/awesome-feature`  
5. Open Pull Request 🙌  

---

## 📜 License  
This project is licensed under the **MIT License**. See the `LICENSE` file.  

---

## 🙏 Acknowledgments  

- [Ultralytics](https://github.com/ultralytics) for YOLOv11  
- [Flask](https://flask.palletsprojects.com/)  
- [OpenCV](https://opencv.org/)  
- [Tailwind CSS](https://tailwindcss.com/)  

---

✨ **Happy Counting!** 🚶‍♀️🚶‍♂️  

import streamlit as st
import os

# Page setup
st.set_page_config(page_title="Person Counter System", layout="wide")
st.title("🚶 Person Counter System")

st.markdown("""
⚡ **Welcome to the Person Counter System Demo on Streamlit Cloud!**  

👉 The full project is built with **Flask + YOLOv11 + OpenCV** to detect and count people in real-time video streams.  
👉 Due to limitations of Streamlit Cloud (no real-time video streaming with OpenCV/Flask),  
this deployment is only a **showcase** of the project.  

---

### 🔧 Run Locally (Full Features)
Clone this repo and run locally to experience the full real-time detection:

```bash
git clone https://github.com/CodingSuru/person-counter-system.git
cd person-counter-system
pip install -r requirements.txt
python main.py""")
import streamlit as st
import os
from PIL import Image

# Dashboard Configuration
st.set_page_config(page_title="VisionGuard AI Dashboard", layout="wide")

st.title("🛡️ VisionGuard AI: Intelligent Surveillance")
st.write("Real-time monitoring and AI threat analysis.")

# Do Columns banayein
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📽️ Live Security Feed")
    st.info("Run 'python main.py' in your terminal to start the AI engine.")
    # Hum yahan placeholder rakh rahe hain kyunki OpenCV window alag khulti hai
    st.image("https://img.freepik.com/premium-photo/cctv-camera-security-system-concept_31965-4330.jpg", use_container_width=True)

with col2:
    st.header("🚨 Intrusion Logs")
    log_dir = "unauthorized"
    
    if os.path.exists(log_dir):
        files = sorted(os.listdir(log_dir), reverse=True)
        if not files:
            st.write("No intrusions detected yet. System is safe! ✅")
        else:
            for file in files[:5]: # Sirf aakhri 5 alerts dikhayega
                with st.container():
                    img_path = os.path.join(log_dir, file)
                    st.image(img_path, caption=f"Detected at: {file}", use_container_width=True)
                    st.divider()
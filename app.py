import streamlit as st
import os
import time
from dotenv import load_dotenv

# Page configuration
st.set_page_config(page_title="VisionGuard AI Dashboard", layout="wide")

# Load keys from .env file (For security)
load_dotenv()

def main():
    st.title("🛡️ VisionGuard AI: Security Dashboard")
    st.sidebar.header("System Status")
    
    # Sidebar status indicators
    if os.getenv("GEMINI_API_KEY"):
        st.sidebar.success("✅ AI Engine: Connected")
    else:
        st.sidebar.error("❌ AI Engine: Disconnected")
        
    if os.getenv("PUSHBULLET_TOKEN"):
        st.sidebar.success("✅ Alerts: Active")
    else:
        st.sidebar.error("❌ Alerts: Offline")

    # Main Dashboard Area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📹 Live Monitoring Analysis")
        st.info("AI is currently scanning the camera feed... (Close the camera window to stop)")
        
        # Create a placeholder for real-time updates
        placeholder = st.empty()
        
        # Here we can simulate logs or read them from a real file
        st.markdown("---")
        st.subheader("📄 Security Incident Logs")
        if os.path.exists("security_logs.txt"):
            with open("security_logs.txt", "r") as f:
                logs = f.readlines()
                for log in reversed(logs[-10:]): # Displays only the last 10 logs
                    st.text(log.strip())
        else:
            st.write("No incidents recorded yet. System is clear.")

    with col2:
        st.subheader("🔔 Quick Actions")
        if st.button("Clear Logs"):
            if os.path.exists("security_logs.txt"):
                os.remove("security_logs.txt")
                st.warning("Logs cleared!")
        
        st.subheader("⚙️ Configuration")
        st.write(f"**Alert Interval:** 20 Seconds")
        st.write(f"**Detection Mode:** Face/Motion")

    # Auto-refresh feature
    time.sleep(2)
    st.rerun()

if __name__ == "__main__":

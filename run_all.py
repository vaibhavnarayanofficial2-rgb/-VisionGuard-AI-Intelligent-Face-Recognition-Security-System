import subprocess
import time
import os
from dotenv import load_dotenv

def start_project():
    # 1. Check karo ki .env file exist karti hai ya nahi
    if not os.path.exists(".env"):
        print("❌ Error: .env file nahi mili! Pehle .env banayein aur API keys dalein.")
        return

    # 2. .env load karke verify karo ki keys khali toh nahi
    load_dotenv()
    if not os.getenv("GEMINI_API_KEY") or not os.getenv("PUSHBULLET_TOKEN"):
        print("❌ Error: .env mein API Keys missing hain!")
        return

    print("🛡️ VisionGuard AI: Security Check Passed!")

    # 3. Dashboard start karo (Streamlit)
    print("🚀 Starting Dashboard...")
    subprocess.Popen(["streamlit", "run", "app.py"])

    # Wait for dashboard to initialize
    time.sleep(5) 

    # 4. Main AI Engine start karo
    print("🧠 Starting AI Guard Engine...")
    try:
        subprocess.run(["python", "main.py"])
    except KeyboardInterrupt:
        print("\n🛑 System shutting down safely...")

if __name__ == "__main__":
    start_project()
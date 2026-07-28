import subprocess
import time
import os
from dotenv import load_dotenv

def start_project():
    # 1. Check if .env file exists
    if not os.path.exists(".env"):
        print("Error: .env file not found! Create .env file and add API keys first.")
        return

    # 2. Load .env and verify that keys are not empty
    load_dotenv()
    if not os.getenv("GEMINI_API_KEY") or not os.getenv("PUSHBULLET_TOKEN"):
        print("Error: API Keys are missing in .env file!")
        return

    print("VisionGuard AI: Security Check Passed!")

    # 3. Start Dashboard (Streamlit)
    print("Starting Dashboard...")
    subprocess.Popen(["streamlit", "run", "app.py"])

    # Wait for dashboard to initialize
    time.sleep(5)

    # 4. Start Main AI Engine
    print("Starting AI Guard Engine...")
    try:
        subprocess.run(["python", "main.py"])
    except KeyboardInterrupt:
        print("\nSystem shutting down safely...")

if __name__ == "__main__":
    start_project()

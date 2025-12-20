import os
import requests
from dotenv import load_dotenv

# .env file se keys load karein
load_dotenv()

# Key ko variable mein load karein
PUSHBULLET_TOKEN = os.getenv("PUSHBULLET_TOKEN")

def send_alert(title, body):
    """
    Naam 'send_alert' rakha hai taaki main.py ka ImportError khatam ho jaye.
    """
    if not PUSHBULLET_TOKEN:
        print("❌ Error: Pushbullet Token .env file mein nahi mila!")
        return

    data = {"type": "note", "title": title, "body": body}
    
    try:
        response = requests.post(
            'https://api.pushbullet.com/v2/pushes',
            json=data,
            headers={'Access-Token': PUSHBULLET_TOKEN},
            timeout=10
        )
        
        if response.status_code == 200:
            print(f"✅ Alert bheja gaya: {title}")
        else:
            print(f"❌ Notification failed! Status: {response.status_code}")
            
    except Exception as e:
        print(f"⚠️ Network Error: {e}")
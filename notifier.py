import os
import requests
from dotenv import load_dotenv

# Load keys from .env file
load_dotenv()

# Load key into variable
PUSHBULLET_TOKEN = os.getenv("PUSHBULLET_TOKEN")

def send_alert(title, body):
    """
    Function name is kept as 'send_alert' to avoid ImportError in main.py.
    """
    if not PUSHBULLET_TOKEN:
        print("Error: Pushbullet Token not found in .env file!")
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
            print(f"Alert sent: {title}")
        else:
            print(f"Notification failed! Status: {response.status_code}")
            
    except Exception as e:
        print(f"Network Error: {e}")

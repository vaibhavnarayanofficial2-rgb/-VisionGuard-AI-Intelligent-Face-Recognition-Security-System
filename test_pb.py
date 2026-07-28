import os
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv("PUSHBULLET_TOKEN")

print(f"Checking Token: {token[:5]}***")

def test_push():
    header = {'Access-Token': token}
    data = {"type": "note", "title": "Test", "body": "Test notification message"}
    
    response = requests.post('https://api.pushbullet.com/v2/pushes', headers=header, json=data)
    
    if response.status_code == 200:
        print("Pushbullet Server accepted the request! Check your phone.")
    else:
        print(f"Error: {response.status_code}")
        print(f"Message: {response.text}")

test_push()

import pyttsx3
import cv2
import os
import time
from ultralytics import YOLO
from deepface import DeepFace
from reporter import get_ai_report 
from notifier import send_alert # WhatsApp ki jagah Pushbullet wala function

# Voice engine setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

# 1. Models aur Folders set karein
model = YOLO('yolov8n.pt') 
db_path = "database" 
save_folder = "unauthorized"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

cap = cv2.VideoCapture(0)
last_captured = 0 

print("🚀 VisionGuard AI Engine is Running... Press 'q' to stop.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, verbose=False)
    
    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                try:
                    face_match = DeepFace.find(frame[y1:y2, x1:x2], db_path=db_path, enforce_detection=False)
                    
                    if len(face_match) > 0 and not face_match[0].empty:
                        name = face_match[0]['identity'][0].split(os.sep)[-1].split('.')[0]
                        label, color = f"STAFF: {name}", (0, 255, 0)
                    else:
                        label, color = "STRANGER ALERT!", (0, 0, 255)
                        
                        current_time = time.time()
                        # Har 20 second mein alert trigger hoga
                        if current_time - last_captured > 20: 
                            # 1. Voice Alarm (Pehle computer bolega)
                            print("🔊 Playing Voice Alert...")
                            engine.say("Alert! Unauthorized person detected")
                            engine.runAndWait()

                            # 2. Push Notification (Phone par turant message jayega)
                            print("📲 Sending Pushbullet Notification...")
                            send_alert(f"⚠️ Security Alert: An unknown person was detected at {time.strftime('%H:%M:%S')}")

                            # 3. Photo Capture
                            timestamp = int(current_time)
                            img_path = f"{save_folder}/intruder_{timestamp}.jpg"
                            cv2.imwrite(img_path, frame)
                            print(f"⚠️ Stranger photo saved at {img_path}")
                            
                            # 4. Gemini Analysis (Reporting)
                            print("🤖 Gemini is analyzing the situation...")
                            report = get_ai_report(img_path)
                            print(f"📄 AI REPORT: {report}\n")
                            
                            last_captured = current_time

                except Exception as e:
                    label, color = "Scanning...", (255, 255, 0)

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("VisionGuard - Live Security Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import pyttsx3
import threading
import time
from notifier import send_alert

# Setup
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml') # Aapki training file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

cap = cv2.VideoCapture(0)
last_alert_time = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Confidence jitna kam hoga, matching utni achi hogi (0 to 100)
        if confidence < 50:
            name = "AUTHORIZED: BOSS"
            color = (0, 255, 0) # Green
        else:
            name = "UNAUTHORIZED!"
            color = (0, 0, 255) # Red
            
            # Alert Logic for Unknown
            current_time = time.time()
            if current_time - last_alert_time > 20:
                threading.Thread(target=speak, args=("Intruder Alert!",)).start()
                send_alert("🚨 Warning", "Unknown person spotted!")
                last_alert_time = current_time

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow('VisionGuard Secure', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
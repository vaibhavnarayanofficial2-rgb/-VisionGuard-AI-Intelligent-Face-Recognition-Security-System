import cv2
import os

# 1. Folder check karo
if not os.path.exists('faces'):
    os.makedirs('faces')

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0
print("📸 Camera ki taraf dekhein aur thoda face move karein...")

while count < 30:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        # Photo save karna
        file_path = f"faces/user.{count}.jpg"
        cv2.imwrite(file_path, gray[y:y+h, x:x+w])
        
        # Rectange dikhana screen par
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('Capturing Faces', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"✅ Success! {count} photos save ho gayi hain 'faces' folder mein.")
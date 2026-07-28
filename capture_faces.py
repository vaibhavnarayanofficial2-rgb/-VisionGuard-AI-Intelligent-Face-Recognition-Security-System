import cv2
import os

# 1. Check folder
if not os.path.exists('faces'):
    os.makedirs('faces')

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0
print("Look towards the camera and move your face slightly...")

while count < 30:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        # Save photo
        file_path = f"faces/user.{count}.jpg"
        cv2.imwrite(file_path, gray[y:y+h, x:x+w])
        
        # Display rectangle on screen
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('Capturing Faces', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Success! {count} photos saved in the 'faces' folder.")

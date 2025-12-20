import cv2
import os
import numpy as np

# Recognizer initialize karein
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []
    for image_path in image_paths:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        faces = detector.detectMultiScale(img)
        for (x, y, w, h) in faces:
            face_samples.append(img[y:y+h, x:x+w])
            ids.append(1) # ID 1 aapke liye hai
    return face_samples, ids

print("⏳ Training faces... Rukiye thoda.")
faces, ids = get_images_and_labels('faces')
recognizer.train(faces, np.array(ids))
recognizer.save('trainer.yml')
print("✅ Training Done! 'trainer.yml' file ban gayi hai.")
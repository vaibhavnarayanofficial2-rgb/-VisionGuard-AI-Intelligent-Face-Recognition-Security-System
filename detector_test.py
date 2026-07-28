import cv2
from ultralytics import YOLO

# 1. Load the lightweight and fast YOLOv8 model
model = YOLO('yolov8n.pt') 

# 2. Turn on the camera
cap = cv2.VideoCapture(0)

print("VisionGuard AI Engine Testing... Press 'q' to stop.")

while True:
    success, frame = cap.read()
    if not success:
        break

    # 3. Send frames to AI for detection
    # We will detect objects like 'person', 'cell phone', 'knife'
    results = model(frame, stream=True)

    for r in results:
        annotated_frame = r.plot() # Automatically creates boxes and labels

    # 4. Display the result
    cv2.imshow("VisionGuard Test Feed", annotated_frame)

    # Press 'q' to close the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

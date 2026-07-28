import cv2
from ultralytics import YOLO

# Load YOLOv8 lightweight model
model = YOLO('yolov8n.pt') 

# Start camera
cap = cv2.VideoCapture(0)

print("VisionGuard AI Engine Testing... Press 'q' to stop.")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Run AI detection on camera frames
    # Detect objects like person, cell phone, knife
    results = model(frame, stream=True)

    for r in results:
        annotated_frame = r.plot()  # Generate detection boxes and labels

    # Show the detection result
    cv2.imshow("VisionGuard Test Feed", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

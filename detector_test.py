import cv2
from ultralytics import YOLO

# 1. YOLOv8 ka sabse light aur fast model load kar rahe hain
model = YOLO('yolov8n.pt') 

# 2. Camera ON karein
cap = cv2.VideoCapture(0)

print("VisionGuard AI Engine Testing... Press 'q' to stop.")

while True:
    success, frame = cap.read()
    if not success:
        break

    # 3. AI ko frame dikhao detection ke liye
    # Hum sirf 'person', 'cell phone', 'knife' jaise objects detect karenge
    results = model(frame, stream=True)

    for r in results:
        annotated_frame = r.plot() # Ye apne aap box aur label bana dega

    # 4. Result dikhao
    cv2.imshow("VisionGuard Test Feed", annotated_frame)

    # 'q' dabane par band ho jayega
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
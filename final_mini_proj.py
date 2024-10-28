import cv2
from ultralytics import YOLO


model_path = r'E:\mini\mini_project\runs\detect\train\weights\best.pt'  # Use a raw string literal


model = YOLO(model_path)


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

   
    results = model(frame)

  
    for result in results:
        annotated_frame = result.plot()

   
    cv2.imshow('YOLOv8 Detection', annotated_frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
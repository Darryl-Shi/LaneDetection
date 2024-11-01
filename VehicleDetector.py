from ultralytics import YOLO

class VehicleDetector:
    def __init__(self, model_path="models/yolo11s.pt", conf_threshold=0.5, iou_threshold=0.5):
        try:
            self.model = YOLO(model_path)
        except FileNotFoundError:
            print(f"YOLO Model not downloaded. Please download the model, then try again.")
            exit()
        self.conf_threshold = conf_threshold
        self.iou_threshold = iou_threshold

    def detect_vehicles(self, frame):
        results = self.model.predict(
            frame, conf=self.conf_threshold, iou=self.iou_threshold
        )
        detections = results[0].boxes.cpu().numpy()
        vehicle_boxes = []
        for detection in detections:
            cls = int(detection.cls)
            if cls in [2, 3, 5, 7]:  # Assuming COCO classes for vehicles
                x1, y1, x2, y2 = detection.xyxy[0]
                vehicle_boxes.append((x1, y1, x2, y2))
        return vehicle_boxes

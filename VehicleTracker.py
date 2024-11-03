import cv2


class VehicleTracker:
    def __init__(self):
        self.vehicle_counts = {}
        for lane in ["Lane 1", "Lane 2", "Lane 3"]:
            self.vehicle_counts[lane] = 0

    def update_counts(self, vehicle_boxes, lanes):
        # Simple logic: increment count if vehicle center is within lane region
        for box in vehicle_boxes:
            x1, y1, x2, y2 = box
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2

            for lane_name, lane_coords in lanes.items():
                # Define lane boundaries and check if vehicle is within
                lane_x1, lane_y1 = lane_coords[0]
                lane_x2, lane_y2 = lane_coords[1]
                if lane_x1 <= cx <= lane_x2:
                    self.vehicle_counts[lane_name] += 1
        return self.vehicle_counts

    def draw_vehicle_counts(self, frame):
        y_offset = 30
        text = "road is congested"
        cv2.putText(
            frame,
            text,
            (10, y_offset),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )
        for lane_name, count in self.vehicle_counts.items():
            #text = f"{lane_name}: {count} vehicles"
            y_offset += 30
        return frame

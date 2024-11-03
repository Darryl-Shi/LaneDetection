## Bangzhen has special needs
from VideoProcessor import VideoProcessor
from VehicleDetector import VehicleDetector
from LaneDetector import LaneDetector
from VehicleTracker import VehicleTracker
from ParameterTuner import ParameterTuner
from DataLogger import DataLogger
import cv2

def main():
    # Initialization
    input_video_path = "videos/fully-congested.mp4"
    output_video_path = "output/output_video.mp4"
    csv_log_path = "output/vehicle_counts.csv"

    video_processor = VideoProcessor(input_video_path, output_video_path)
    vehicle_detector = VehicleDetector()
    lane_detector = LaneDetector()
    vehicle_tracker = VehicleTracker()
    parameter_tuner = ParameterTuner()
    data_logger = DataLogger(csv_log_path)

    frame_number = 0
    
    while True:
        frame = video_processor.read_frame()
        if frame is None:
            break

        # Detect vehicles
        conf_threshold, iou_threshold = parameter_tuner.get_parameters()
        vehicle_detector.conf_threshold = conf_threshold
        vehicle_detector.iou_threshold = iou_threshold
        vehicle_boxes = vehicle_detector.detect_vehicles(frame)

        # Detect lanes
        lanes = lane_detector.detect_lanes(frame)

        # Update vehicle counts
        vehicle_counts = vehicle_tracker.update_counts(vehicle_boxes, lanes)

        # Draw bounding boxes
        for box in vehicle_boxes:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Draw lanes
        frame = lane_detector.draw_lanes(frame, lanes)

        # Draw vehicle counts
        frame = vehicle_tracker.draw_vehicle_counts(frame)

        # Log data
        data_logger.log_frame_data(frame_number, vehicle_counts)
        
        # Write frame to output video
        video_processor.write_frame(frame)
        # Display live feed
        width = int(video_processor.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video_processor.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        window_width, window_height = 1600, int(1600 * (height / width))
        display_frame = cv2.resize(frame, (window_width, window_height))
        cv2.imshow("Processed Video", display_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        frame_number += 1

    # Release resources
    video_processor.release_resources()
    data_logger.save_to_csv()

if __name__ == "__main__":
    main()
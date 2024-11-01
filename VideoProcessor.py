import cv2


class VideoProcessor:
    def __init__(self, input_video_path, output_video_path):
        self.input_video_path = input_video_path
        self.output_video_path = output_video_path
        self.cap = cv2.VideoCapture(self.input_video_path)
        # Video Writer will be initialized after reading video properties

    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def write_frame(self, frame):
        if not hasattr(self, "out"):
            # Initialize VideoWriter with properties matching the input video
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            fps = self.cap.get(cv2.CAP_PROP_FPS)
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.out = cv2.VideoWriter(
                self.output_video_path, fourcc, fps, (width, height)
            )
        self.out.write(frame)

    def release_resources(self):
        self.cap.release()
        if hasattr(self, "out"):
            self.out.release()
        cv2.destroyAllWindows()

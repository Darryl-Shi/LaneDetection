import pandas as pd


class DataLogger:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.data = []

    def log_frame_data(self, frame_number, vehicle_counts):
        entry = {"frame": frame_number}
        entry.update(vehicle_counts)
        self.data.append(entry)

    def save_to_csv(self):
        df = pd.DataFrame(self.data)
        df.to_csv(self.csv_path, index=False)

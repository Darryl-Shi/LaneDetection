class ParameterTuner:
    def __init__(self):
        self.conf_threshold = 0.3
        self.iou_threshold = 0.3

    def set_conf_threshold(self, value):
        self.conf_threshold = value

    def set_iou_threshold(self, value):
        self.iou_threshold = value

    def get_parameters(self):
        return self.conf_threshold, self.iou_threshold

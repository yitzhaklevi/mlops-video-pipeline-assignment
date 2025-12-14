import os
from tempfile import gettempdir
from ultralytics import YOLO
import torch

class PedestrianDetectionModel:
    DEFAULT_MODEL = "yolov8s"
    SUPPORTED_MODELS = {"yolov8n", "yolov8s", "yolov8m", "yolov8l", "yolov8x"}
    PERSON_CLASS_ID = 0  # COCO dataset person class

    def __init__(self, model_name: str = DEFAULT_MODEL, confidence_threshold: float = 0.5):
        assert model_name in self.SUPPORTED_MODELS, f"Unsupported model: {model_name}"
        self.model_name = model_name
        self.confidence_threshold = confidence_threshold
        self.cache_dir = os.path.join(gettempdir(), "mlops-video-pipeline-assignment")
        self.model_path = os.path.join(self.cache_dir, f"{self.model_name}.pt")
        self.model = YOLO(self.model_path)
    
    def get_detections(self, frames: torch.Tensor, confidence_threshold: float = None) -> list[dict]:
        if confidence_threshold is None:
            confidence_threshold = self.confidence_threshold
        return self.model(frames, conf=confidence_threshold, classes=[self.PERSON_CLASS_ID], verbose=False)


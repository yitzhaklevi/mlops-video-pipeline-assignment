# https://huggingface.co/docs/transformers/en/model_doc/vitpose


import cv2
import numpy as np
import torch
from PIL import Image
from transformers import AutoProcessor, VitPoseForPoseEstimation


class PoseEstimationModel:
    DEFAULT_MODEL = "usyd-community/vitpose-base-simple"

    def __init__(self, model_name: str = DEFAULT_MODEL):
        self.model_name = model_name
        self.model = VitPoseForPoseEstimation.from_pretrained(self.model_name)
        self.processor = AutoProcessor.from_pretrained(self.model_name, use_fast=False)
        self.model.eval()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def _prepare_image(self, image):
        """Convert image to PIL Image format."""
        if isinstance(image, np.ndarray):
            # Convert BGR to RGB if it's a color image
            if len(image.shape) == 3 and image.shape[2] == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return Image.fromarray(image)
        return image

    def estimate_pose(self, cropped_image) -> dict:
        """
        Estimate pose for a cropped person image.

        Args:
            cropped_image: Cropped image as numpy array (BGR format from OpenCV)

        Returns:
            Dictionary with 'keypoints' containing list of (x, y) coordinates
        """
        # Convert to PIL Image
        pil_image = self._prepare_image(cropped_image)

        # Get image dimensions for bbox (treating cropped image as full image)
        width, height = pil_image.size
        # COCO format bbox: (x1, y1, w, h)
        coco_bbox = (0, 0, width, height)
        boxes = [[coco_bbox]]  # ViTPose expects list of lists

        # Process image and boxes
        inputs = self.processor(pil_image, boxes=boxes, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        # Run inference
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Post-process results
        pose_results = self.processor.post_process_pose_estimation(outputs, boxes=boxes)

        if not pose_results or not pose_results[0]:
            return {"keypoints": []}

        # Extract keypoints and scores
        pose_result = pose_results[0][0]
        keypoints_tensor = pose_result["keypoints"]  # Shape: (17, 2)
        scores_tensor = pose_result["scores"]  # Shape: (17,)

        # Convert to numpy
        keypoints_np = keypoints_tensor.cpu().numpy()
        scores_np = scores_tensor.cpu().numpy()

        # Format keypoints as list of (x, y) tuples for easy access
        keypoints = [(float(kp[0]), float(kp[1])) for kp in keypoints_np]

        return {"keypoints": keypoints, "scores": scores_np.tolist()}

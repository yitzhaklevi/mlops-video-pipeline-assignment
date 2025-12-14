import cv2 as cv
import numpy as np


class VideoProcessor:

    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv.VideoCapture(video_path)

        self.num_frames_in_video = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
        self.frames_per_second = self.cap.get(cv.CAP_PROP_FPS)
        self.video_length_in_seconds = self.num_frames_in_video / self.frames_per_second

    def get_frame(self, frame_index: int) -> np.ndarray:
        assert (
            frame_index >= 0 and frame_index < self.num_frames_in_video
        ), "Frame index out of bounds"
        self.cap.set(cv.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = self.cap.read()
        assert ret, f"Failed to read frame {frame_index}"
        return frame

    def __del__(self):
        self.cap.release()

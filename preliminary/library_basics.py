"""A basic introduction to Open CV

Instructions
------------

Implement the functions below based on their docstrings.

Notice some docstrings include references to third-party documentation
Some docstrings **require** you to add references to third-party documentation.

Make sure you read the docstrings C.A.R.E.F.U.L.Y (yes, I took the L to check that you are awake!)
"""

from PIL import Image
from pathlib import Path
import cv2
import numpy as np


VID_PATH = Path("resources/oop.mp4")

class CodingVideo:
    capture: cv2.VideoCapture


    def __init__(self, video: Path | str):
        self.capture = cv2.VideoCapture(str(video))
        if not self.capture.isOpened():
            raise ValueError(f"Cannot open {video}")

        self.fps = float(self.capture.get(cv2.CAP_PROP_FPS))
        self.frame_count = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps if self.fps > 0 else 0.0


    def __str__(self) -> str:
        """Displays key metadata from the video

        Specifically, the following information is shown:
            FPS - Number of frames per second rounded to two decimal points
            FRAME COUNT - The total number of frames in the video
            DURATION (minutes) - Calculated total duration of the video given FPS and FRAME COUNT

        Reference
        ----------
        https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        """
        return (
            f"FPS: {self.fps:.2f}\n"
            f"FRAME COUNT: {self.frame_count}\n"
            f"DURATION (minutes): {self.duration / 60:.1f}"
        )

    def get_frame_number_at_time(self, seconds: int) -> int:
        """Given a time in seconds, returns the value of the nearest frame"""
        if seconds < 0:
            raise ValueError("seconds must be non-negative")
        return int(seconds * self.fps)


    def get_frame_rgb_array(self, frame_number: int) -> np.ndarray:
        """Returns a numpy N-dimensional array (ndarray)

        The array represents the RGB values of each pixel in a given frame

        Note: cv2 defaults to BGR format, so this function converts the color space to RGB

        Reference
        ---------
        https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
        """
        if frame_number < 0 or frame_number >= self.frame_count:
            raise ValueError("frame_number is out of range")

        self.capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Failed to read requested frame")

        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def get_image_as_bytes(self, seconds: int) -> bytes:
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.get_frame_number_at_time(seconds))
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame in target location")
        ok, buf = cv2.imencode(".png", frame)
        if not ok:
            raise ValueError("Failed to encode frame")
        return buf.tobytes()

    def save_as_image(self, seconds: int, output_path: Path | str = 'output.png') -> None:
        """Save the frame at a given time as a PNG image.

        Uses Pillow to convert the NumPy frame array into a PNG file.
        Reference:
        https://pillow.readthedocs.io/en/stable/reference/Image.html
        """
        frame_number = self.get_frame_number_at_time(seconds)
        frame = self.get_frame_rgb_array(frame_number)

        try:
            image = Image.fromarray(frame)
            image.save(output_path)
        except Exception as exc:
            raise ValueError(f"Failed to save image to {output_path}") from exc
        

def test():
    """Try out your class here"""
    oop = CodingVideo(VID_PATH)
    print(oop)
    # print(oop.get_frame_rgb_array(42))
    oop.save_as_image(242)

if __name__ == '__main__':
    test()

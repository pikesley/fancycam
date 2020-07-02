import time

from camera.base_camera import BaseCamera

dummy_frames = "camera/dummy_frames"


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    imgs = [open(f"{dummy_frames}/{f}.jpg", "rb").read() for f in ["1", "2", "3"]]

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            yield Camera.imgs[int(time.time()) % 3]

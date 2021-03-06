import os

from flask import Response, render_template

from fancycam import app

# import camera driver
if os.uname().machine.startswith("arm"):
    from camera.camera_pi import Camera
else:
    from camera.camera import Camera


@app.route("/")
@app.route("/index")
def index():
    """The noddiest route."""
    return render_template("index.html", title="FancyCam")


@app.route("/video_feed")
def video_feed():
    """Route for video feed."""
    return Response(gen(Camera()), mimetype="multipart/x-mixed-replace; boundary=frame")


def gen(cam):
    """Yield frames from camera."""
    while True:
        frame = cam.get_frame()
        yield b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"

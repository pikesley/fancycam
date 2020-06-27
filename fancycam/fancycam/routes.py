from flask import render_template

from fancycam import app


@app.route("/")
@app.route("/index")
def index():
    """The noddiest route."""
    return render_template("index.html", title="FancyCam", bulma_version="0.9.0")

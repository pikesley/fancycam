from fancycam import app


@app.route("/")
@app.route("/index")
def index():
    """The noddiest route."""
    return "Hello, World!"

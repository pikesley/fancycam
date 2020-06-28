import os

import sass
from flask import Flask
from sassutils.wsgi import SassMiddleware

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

if "PLATFORM" in os.environ:
    if os.environ["PLATFORM"] == "docker":
        app.wsgi_app = SassMiddleware(
            app.wsgi_app,
            {
                "fancycam": {
                    "sass_path": "static/sass",
                    "css_path": "static/css",
                    "wsgi_path": "/static/css",
                    "strip_extension": True,
                }
            },
        )


from fancycam import routes  # isort:skip;pylint:disable=C0413,R0401

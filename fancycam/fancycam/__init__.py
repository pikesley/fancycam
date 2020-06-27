from flask import Flask

app = Flask(__name__)

from fancycam import routes  # isort:skip;pylint:disable=C0413,R0401

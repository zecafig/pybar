import os
from flask import Flask

from config import basedir
from app.views import app as home


def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join(basedir, "resources", "static"),
        template_folder=os.path.join(basedir, "resources", "templates")
    )

    app.register_blueprint(home)

    return app

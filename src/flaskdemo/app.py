from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
import time
import sys
from flaskdemo.configuration import config
import os

UPLOAD_FOLDER = "/tmp"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "json"}

# static_url_path="/static", template_folder="./templates"
app = Flask(__name__)

app.config.update(config().as_dict())
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "HaHA($(#$$33--"

db = SQLAlchemy(app)

from flaskdemo.controllers.movies import movies_blueprint
from flaskdemo.controllers.actors import actors_blueprint

app.register_blueprint(movies_blueprint)
app.register_blueprint(actors_blueprint)

if __name__ == "__main__":
    os.environ["FLASK_ENV"] = "development"
    os.environ["FLASK_APP"] = "app"
    app.run(debug=True)

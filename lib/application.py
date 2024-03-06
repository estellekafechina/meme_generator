
from flask import Flask
from .db import configure_db
from .base import Application

@configure_db( migrate= True)
def create_application(name, config: dict =None) :
    app = Flask(name)
    if config is not None:
        for key in config:
            app.config[key] = config.get(key)
    return Application (app)

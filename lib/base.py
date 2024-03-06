from flask import Flask , Blueprint
from flask_sqlalchemy import  SQLAlchemy


class Application():
    def __init__(self,app : Flask , db : SQLAlchemy = None):
        self.wsgi = None 
        if app is not None : 
            self.init_app(app)
        self.db = db 
        
    def set_db(self ,db : SQLAlchemy ):
        self.db = db
    
    def init_app(self, app : Flask):
        self.wsgi=app

    def register_module(self , module :Blueprint, **kwargs):
        self.wsgi.register_blueprint(module, **kwargs)
        
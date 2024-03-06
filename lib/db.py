#configurer la bd 

from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import Migrate
from .base import Application

def configure_db(migrate: bool = False):

    def decorate_decorator(func):
        def decorate(*args , **kwargs):
            app = func(*args , **kwargs)
            if not isinstance(app , Application):
                raise Exception ('expect factory function to return an instance of flask')
            app.set_db(SQLAlchemy(app.wsgi))
            if migrate == True :
                Migrate(app.wsgi , app.db)
                
            return app 
        return decorate
    return decorate_decorator
            



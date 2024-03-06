#configuration des prerequis de l'application

from lib  import create_application 
application = create_application(__name__,{
      'SQLALCHEMY_DATABASE_URI':"mysql://root:root@localhost:3306/meme_generator",
      'SQLALCHEMY_TRACK_MODIFICATIONS': False
   })
kernel=application.wsgi
db = application.db




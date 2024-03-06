from config import kernel
from controllers.meme import meme_blueprint
from controllers.home import home_blueprint
from models import *
app=kernel

app.register_blueprint(meme_blueprint, url_prefix='/meme')
app.register_blueprint(home_blueprint)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  





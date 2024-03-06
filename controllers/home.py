
from flask import Blueprint, render_template

from models import Meme

home_blueprint = Blueprint('home', __name__ ,template_folder='templates')

@home_blueprint.route('/home',methods=['GET'])
def home():
    condition = True 
    if condition:
        return render_template('index.html')
    else:
        return "Condition non remplie", 404
    

@home_blueprint.route('/galery')
def gallery():
    memes = Meme.query.all()
    return render_template('index.html', memes=memes)

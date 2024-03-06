from flask import Blueprint, Flask, current_app, render_template, request
from PIL import Image, ImageDraw, ImageFont
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
meme_blueprint = Blueprint('meme', __name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@meme_blueprint.route('/create-meme', methods=['POST'])
def create_meme():
    image_file = request.files['image']
    text = request.form['text']
    max_size = (800, 800)  # Taille maximale de l'image en pixels

    if image_file:
        filename = secure_filename(image_file.filename)
        upload_folder = os.path.join(current_app.static_folder, 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        image_path = os.path.join(upload_folder, filename)

        image = Image.open(image_file.stream)

        # Redimensionner l'image tout en préservant le ratio d'aspect
        image.thumbnail(max_size, Image.LANCZOS)  # Utilisez Image.LANCZOS

        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((20, 20), text, fill="white", font=font)

        image.save(image_path, 'JPEG')

        rel_image_path = os.path.join('uploads', filename)

        return render_template('index.html', image_path=rel_image_path)

    return "Aucune image fournie", 400

if __name__ == "__main__":
    app.run(debug=True)

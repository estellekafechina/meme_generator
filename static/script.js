document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.querySelector('input[type="file"]');
    const textInput = document.querySelector('input[type="text"]');
    const imagePreview = document.getElementById('image-preview');
    const textPreview = document.getElementById('text-preview');

    // Afficher l'image choisie dans l'aperçu
    imageInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imagePreview.style.display = 'block';
            }
            reader.readAsDataURL(this.files[0]);
        }
    });

    // Mettre à jour le texte de l'aperçu en temps réel
    textInput.addEventListener('keyup', function() {
        textPreview.innerText = this.value;
        positionText(); // Positionnez le texte correctement si nécessaire
    });

    // Fonction pour positionner le texte sur l'image
    function positionText() {
        // Vous pouvez ajuster la position du texte ici si nécessaire
        textPreview.style.top = '50%';
        textPreview.style.left = '50%';
        textPreview.style.transform = 'translate(-50%, -50%)';
        textPreview.style.color = 'white'; // Modifier la couleur du texte si nécessaire
    }
});

document.getElementById('imageInput').addEventListener('change', function(event) {
    const reader = new FileReader();
    reader.onload = function() {
        const img = new Image();
        img.onload = function() {
            drawMeme(img);
        };
        img.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
});

document.getElementById('textInput').addEventListener('input', function() {
    const img = new Image();
    img.onload = function() {
        drawMeme(img);
    };
    img.src = document.getElementById('imageInput').files[0] ? URL.createObjectURL(document.getElementById('imageInput').files[0]) : "";
});

function drawMeme(img) {
    const canvas = document.getElementById('memeCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0);
    ctx.font = '40px Arial';
    ctx.fillStyle = 'white';
    ctx.textAlign = 'center';
    ctx.fillText(document.getElementById('textInput').value, canvas.width / 2, canvas.height - 40);
}

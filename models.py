from config import db 


class MemeGenerator(db.Model):
    __tablename__ = "memes"

    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(255), nullable=True)

    def __json__(self):
        return {
            "id": self.id,
            "image_path": self.image_path,
            "text": self.text
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Meme(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(255), nullable=True)
    def __json__(self):
        return {
            "id": self.id,
            "image_path": self.image_path,
            "text": self.text
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
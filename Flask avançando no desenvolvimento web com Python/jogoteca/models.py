from jogoteca import db
class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=True)
    categoria = db.Column(db.String(40), nullable=True)
    console = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<Name %r' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=True)
    senha = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<Name %r' % self.name

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):

    __tablename__ = 'usuarios'
    
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
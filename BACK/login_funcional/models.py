from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Evento(db.Model):
    __tablename__ = 'eventos'
    
    id_evento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_evento = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    entradas_disponibles = db.Column(db.Integer, nullable=False)
    localizacion = db.Column(db.String(50), nullable=False)
    precio_entrada = db.Column(db.Numeric(5, 2), nullable=False)

class Reserva(db.Model):
    __tablename__ = 'reservas'
    
    id_reserva = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_evento = db.Column(db.Integer, db.ForeignKey('eventos.id_evento'), nullable=False)
    cant_tickets = db.Column(db.Integer, nullable=False)
    
    # Relación con el modelo Usuario
    usuario = db.relationship('Usuario', backref=db.backref('reservas', lazy=True))
    # Relación con el modelo Evento
    evento = db.relationship('Evento', backref=db.backref('reservas', lazy=True))
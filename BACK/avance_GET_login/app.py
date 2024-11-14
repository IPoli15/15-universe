from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from config import Config
from models import db, Usuario

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

""" with app.app_context():
    db.create_all() """

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        
        # Buscar el usuario en la base de datos
        usuario = Usuario.query.filter_by(nombre=nombre).first()
        
        if usuario and usuario.password == password:
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')
            return redirect(url_for('login'))
    
    # Renderizar el template de login en caso de petición GET
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "¡Bienvenido al Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import Config
from models import db, Usuario
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
# Recordar que los datos de la db en cuanto a nombre, usuario y contraseña varian.
engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/universe")

#--------------------------------------------------------TABLA USUARIOS-----------------------------------#

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
        
        if usuario:
            print(f"Usuario encontrado: {usuario.nombre}, {usuario.password}")
        else:
            print("Usuario no encontrado")
        
        if usuario and usuario.password == password:
            print("Contraseña correcta")
            return redirect(url_for('index'))
        else:
            print("Contraseña incorrecta o usuario no encontrado")
            return redirect(url_for('login'))
    
    # Renderizar el template de login en caso de petición GET
    return render_template('login.html')

#---------------------------------------------------------------------------------------------------------#

@app.route('/musica')
def musica():
    return render_template('musica.html')

@app.route('/cultura_jp')
def cultura_jp():
    return render_template('cultura_jp.html')

@app.route('/fiestas')
def fiestas():
    return render_template('fiestas.html')

@app.route('/eSports')
def esports():
    return render_template('eSports.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/reserva')
def Reserva():
    return render_template('reserva.html')

@app.route('/pago')
def Pago():
    return render_template('pago.html')

@app.route('/futbol')
def Futbol():
    return render_template('futbol.html')

@app.route('/stand-up')
def Stand_up():
    return render_template('stand_up.html')

@app.route('/teatro')
def Teatro():
    return render_template('Teatro.html')

@app.route('/tu-reserva')
def Tu_reserva():
    nombre="Juan Perez"
    dni="42100124"
    codigo_reserva="ab1224"
    sector="7B"
    cantidad_tickets=2
    precio_total = "$40.000"
    return render_template('tu-reserva.html', nombre=nombre,dni=dni, codigo_reserva=codigo_reserva, sector=sector, cantidad_tickets=cantidad_tickets, precio_total=precio_total)

#---------------------------------------------------------------------------------------------------------#

# Esta ruta es solo para probar la conexión a la base de datos,
# si no esta correctamente conectada devolverá un error.
@app.route('/test_db')
def test_db():
    try:
        result = db.session.execute(text('SELECT 1'))
        return 'Database connection successful!'
    except SQLAlchemyError as e:
        return str(e)

#---------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)
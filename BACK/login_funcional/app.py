from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import Config
from models import db, Usuario, Evento, Reserva
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
# Recordar que los datos de la db en cuanto a nombre, usuario y contraseña varian.
engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/universe")

# Variable para validar si es admin o no,
# app.config es un diccionario especial de flask para almacenar configuraciones de la aplicación,
# estas estan disponibles en toda la aplicacion y son accesibles desde cualquier parte de la misma
app.config['ES_ADMIN'] = False


#--------------------------------------------------------TABLA USUARIOS-----------------------------------#

@app.route('/')
def index():
    return render_template('index.html', es_admin=app.config['ES_ADMIN'])

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
            app.config['ES_ADMIN'] = True
            return redirect(url_for('index'))
        else:
            print("Contraseña incorrecta o usuario no encontrado")
            return redirect(url_for('login'))
    
    return render_template('login.html')

#---------------------------------------------------------------------------------------------------------#

@app.route('/conciertos')
def conciertos():
    return render_template('conciertos.html', es_admin=app.config['ES_ADMIN'])

@app.route('/musica')
def musica():
    return render_template('musica.html', es_admin=app.config['ES_ADMIN'])

@app.route('/cultura_jp')
def cultura_jp():
    return render_template('cultura_jp.html', es_admin=app.config['ES_ADMIN'])

@app.route('/fiestas')
def fiestas():
    return render_template('fiestas.html', es_admin=app.config['ES_ADMIN'])

@app.route('/eSports')
def esports():
    return render_template('eSports.html', es_admin=app.config['ES_ADMIN'])

@app.route('/error')
def error():
    return render_template('error.html', es_admin=app.config['ES_ADMIN'])

@app.route('/reserva')
def reserva():
    return render_template('reserva.html', es_admin=app.config['ES_ADMIN'])

#--------------------------------------------------------TABLA RESERVAS-----------------------------------#

@app.route('/pago', methods=['GET', 'POST'])
def Pago():
    if request.method == 'POST':
        # Creo variables para almacenar los datos del formulario:
        nombre = request.form['nombre']
        id_evento = request.form['id_evento']
        cant_tickets = request.form['cant_tickets']

        # Si el usuario y el id del evento existen en la base de datos, entonces crea una reserva:
        try:

            id_usuario = Usuario.query.filter_by(nombre=nombre).first().id_usuario

            nueva_reserva = Reserva(id_usuario=id_usuario, id_evento=id_evento, cant_tickets=cant_tickets)
            db.session.add(nueva_reserva)
            db.session.commit()

            # Por si se quiere validar la información de la reserva creada:
            """ print(f"Reserva creada: ID reserva: {nueva_reserva.id_reserva}")
            print(f"Usuario: {nombre}")
            print(f"ID usuario: {id_usuario}")
            print(f"Evento: {Evento.query.filter_by(id_evento=id_evento).first().nombre_evento}")
            print(f"ID evento: {id_evento}")
            print(f"Cantidad de tickets: {cant_tickets}") """

            return redirect(url_for('Tu_reserva'))
        
        # Si alguno de los dos no existe entonces devuelve un error y deja al usuario en el mismo html.
        except:
            print("Error al crear la reserva")
        
    return render_template('pago.html', es_admin=app.config['ES_ADMIN'])
#---------------------------------------------------------------------------------------------------------#

@app.route('/futbol')
def Futbol():
    return render_template('futbol.html', es_admin=app.config['ES_ADMIN'])

@app.route('/stand-up')
def Stand_up():
    return render_template('stand_up.html', es_admin=app.config['ES_ADMIN'])

@app.route('/teatro')
def Teatro():
    return render_template('Teatro.html', es_admin=app.config['ES_ADMIN'])

@app.route('/tu-reserva')
def Tu_reserva():
    nombre="Juan Perez"
    dni="42100124"
    codigo_reserva="ab1224"
    sector="7B"
    cantidad_tickets=2
    precio_total = "$40.000"
    return render_template('tu-reserva.html', nombre=nombre,dni=dni, codigo_reserva=codigo_reserva, sector=sector, cantidad_tickets=cantidad_tickets, precio_total=precio_total, es_admin=app.config['ES_ADMIN'])

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
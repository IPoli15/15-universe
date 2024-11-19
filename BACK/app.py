from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from config import Config
from models import db, Usuario, Evento, Reserva
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

QUERY_RESERVA_BY_ID = "SELECT id_usuario, id_evento, cant_tickets FROM reservas WHERE id_reserva = :id_reserva"
QUERY_INGRESAR_RESERVA = "INSERT INTO reservas (id_usuario, id_evento, id_reserva, cant_tickets) VALUES (:id_usuario, :id_evento,  :id_reserva, :cant_tickets)"
QUERY_ELIMINAR_RESERVA = "DELETE FROM reservas WHERE id_reserva = :id_reserva"
QUERY_RESERVAS_EVENTO = "SELECT COUNT(*) FROM eventos WHERE id_evento = :id_evento"
QUERY_ELIMINAR_EVENTO = "DELETE FROM eventos WHERE id_evento = :id_evento"
QUERY_TODAS_LAS_RESERVAS = """SELECT R.id_reserva, R.cant_tickets, U.nombre, E.nombre_evento, E.precio_entrada FROM reservas R
INNER JOIN usuarios U on U.id_usuario = R.id_usuario
INNER JOIN eventos E on E.id_evento = R.id_evento"""
QUERY_TODOS_LOS_EVENTOS = " SELECT id_evento, nombre_evento, categoria, descripcion, entradas_disponibles, localizacion, precio_entrada from eventos "
QUERY_EVENTOS_POR_CATEGORIA = "SELECT id_evento, nombre_evento, categoria, descripcion, entradas_disponibles, localizacion, precio_entrada FROM eventos WHERE categoria = :categoria"

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
# Recordar que los datos de la db en cuanto a nombre, usuario y contraseña varian.
engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/universe")

def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()

    return result

@app.route('/')
def index():
    return render_template('index.html')

#--------------------------------------------------------TABLA USUARIOS-----------------------------------#

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


#--------------------------------------------------------TABLA RESERVAS-----------------------------------#


#----METODO GET, CONSULTAR RESERVA POR ID DE RESERVA -----#

def reserva_by_id(id_reserva):
    return run_query(QUERY_RESERVA_BY_ID, {'id_reserva': id_reserva}).fetchall()

@app.route('/consultar-reserva/<int:id_reserva>', methods=['GET'])
def consultar_reserva(id_reserva):
    try:
        result = reserva_by_id(id_reserva)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    if len(result) == 0:
        return jsonify({'error': 'No se encontró la reserva'}), 404 # Not found

    result = result[0]
    return jsonify({'id_usuarios': result[0], 'id_evento': result[1], 'cant_tickets': result[2]}), 200

#----METODO GET, CONSULTAR TODAS LAS RESERVAS -----#

def reservas():
    return run_query(QUERY_TODAS_LAS_RESERVAS).fetchall()

@app.route('/consultar-reservas', methods=['GET'])
def obtener_reservas():
    try:
        result = reservas()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    response = []
    for row in result:
        response.append({'id_reserva': row[0], 'cant_tickets': row[1], 'nombre_usuario': row[2], 'nombre_evento': row[3], 'precio_entradda':row[4]})

    return jsonify(response), 200


#---METODO POST, INSERTAR RESERVAS ----#


def insertar_reserva(data):
    run_query(QUERY_INGRESAR_RESERVA, data)

@app.route('/crear-reserva', methods=['POST'])
def add_reserva():
    data = request.get_json()

    keys = ('id_usuarios', 'id_evento', 'id_reserva', 'cant_tickets')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Falta el dato {key}'}), 400

    try:
        result = reserva_by_id(data['id_reserva'])
        if len(result) > 0:
            return jsonify({'error': 'La reserva ya existe'}), 400

        insertar_reserva(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(data), 201

#---METODO DELETE, ELIMINAR RESERVA ----#


@app.route('/eliminar-reserva/<int:id_reserva>', methods=['DELETE'])
def eliminar_reserva(id_reserva):
    try:
    
        result = run_query(QUERY_ELIMINAR_RESERVA, {'id_reserva': id_reserva})

        if result.rowcount == 0:
            return jsonify({'error': 'No se encontró una reserva con este ID'}), 404

        return jsonify({'mensaje': f'La reserva ID {id_reserva} fue eliminada'}), 200
    
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

#--------------------------------------------------------TABLA EVENTOS-----------------------------------#

def eventos_por_categoria(categoria):
    return run_query(QUERY_EVENTOS_POR_CATEGORIA, {'categoria': categoria}).fetchall()

@app.route('/consultar-eventos/<string:categoria>', methods=['GET'])
def consultar_eventos_por_categoria(categoria):
    try:
        result = eventos_por_categoria(categoria)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    if len(result) == 0:
        return jsonify({'error': 'No se encontró eventos'}), 404 # Not found

    response = []
    for row in result:
        response.append({'id_evento': row[0], 'nombre_evento': row[1], 'categoria': row[2], 'descripcion': row[3], 'entradas_disponibles':row[4], 'localizacion':row[5], 'precio_entrada':row[6]})
    return jsonify(response), 200


def eventos():
    return run_query(QUERY_TODOS_LOS_EVENTOS).fetchall()

@app.route('/consultar-eventos', methods=['GET'])
def obtener_eventos():
    try:
        result = eventos()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    response = []
    for row in result:
        response.append({'id_evento': row[0], 'nombre_evento': row[1], 'categoria': row[2], 'descripcion': row[3], 'entradas_disponibles':row[4], 'localizacion':row[5], 'precio_entrada':row[6]})

    return jsonify(response), 200


@app.route('/eliminar-evento/<int:id_evento>', methods=['DELETE'])
def eliminar_evento(id_evento):
    try:      
        result_reservas = run_query(QUERY_RESERVAS_EVENTO, {'id_evento': id_evento}).fetchone()

        if result_reservas[0] > 0:
        
            run_query(QUERY_ELIMINAR_RESERVA, {'id_evento': id_evento})
        
        result = run_query(QUERY_ELIMINAR_EVENTO, {'id_evento': id_evento})

        if result.rowcount == 0:
            return jsonify({'error': 'No se encontró un evento con este ID'}), 404

        return jsonify({'mensaje': f'El evento ID {id_evento} fue eliminado junto con sus reservas'}), 200
    
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
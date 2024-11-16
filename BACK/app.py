from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import check_password_hash
from config import Config
from models import db, Usuario
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

QUERY_RESERVA_BY_ID = "SELECT id_usuarios, id_evento, cant_tickets FROM reservas WHERE id_reserva = :id_reserva"
QUERY_INGRESAR_RESERVA = "INSERT INTO reservas (id_usuarios, id_evento, id_reserva, cant_tickets) VALUES (:id_usuarios, :id_evento,  :id_reserva, :cant_tickets)"
QUERY_ELIMINAR_RESERVA = "DELETE FROM reservas WHERE id_reserva = :id_reserva"
QUERY_RESERVAS_EVENTO = "SELECT COUNT(*) FROM eventos WHERE id_evento = :id_evento"
QUERY_ELIMINAR_EVENTO = "DELETE FROM eventos WHERE id_evento = :id_evento"

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

engine = create_engine("mysql+mysqlconnector://root:tuclave@localhost:3306/universe")

def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()

    return result

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
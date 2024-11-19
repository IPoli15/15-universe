from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

# Configuración
app = Flask(__name__, template_folder='../FRONT/templates', static_folder='../FRONT/static')
app.secret_key = 'coqui2529'
engine = create_engine("mysql+mysqlconnector://root:coqui2529@localhost:3306/universe")

# Queries SQL
QUERY_CREAR_EVENTO = """
    INSERT INTO eventos (nombre_evento, categoria, descripcion, entradas_disponibles, localizacion, precio_entrada)
    VALUES (:nombre_evento, :categoria, :descripcion, :entradas_disponibles, :localizacion, :precio_entrada)
"""

def run_query(query, parameters=None):
    with engine.connect() as conn:
        print(f"Ejecutando consulta: {query} con parámetros: {parameters}")
        result = conn.execute(text(query), parameters)
        conn.commit()
    return result


@app.route('/crear_evento', methods=['POST'])
def crear_evento():
    data = {
        'nombre_evento': request.form['nombre_evento'],
        'categoria': request.form['categoria'],
        'descripcion': request.form['descripcion'],
        'entradas_disponibles': request.form['entradas_disponibles'],
        'localizacion': request.form['localizacion'],
        'precio_entrada': request.form['precio_entrada']
    }

    try:
        run_query(QUERY_CREAR_EVENTO, data)
        flash('Evento creado con éxito.', 'success')
    except SQLAlchemyError as e:
        flash(f'Error al crear el evento: {e}', 'danger')

    return redirect(url_for('crear_evento_form'))

if __name__ == '__main__':
    app.run(debug=True, port=5001) 

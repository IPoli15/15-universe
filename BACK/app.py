from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, template_folder='../FRONT/templates') 


# config para conectarme a mi base de datos o con la de ustedes
db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'coqui2529', 
    'database': 'eventos'
}

def connectionBD():
    return mysql.connector.connect(**db_config)

# mostrar el formulario de creacion de evento
@app.route('/crear_evento')
def crear_evento_form():
    return render_template('crear_evento.html')

# ruta para procesar el formulario de creacion de evento (POST)
@app.route('/crear_evento', methods=['POST'])
def crear_evento():
    if request.method == 'POST':
        # obtener los datos del formulario
        nombre_evento = request.form['nombre_evento']
        categoria = request.form['categoria']
        descripcion = request.form['descripcion']
        entradas_disponibles = request.form['entradas_disponibles']
        localizacion = request.form['localizacion']
        precio_entrada = request.form['precio_entrada']

        # conectar a la base de datos
        conexion = connectionBD()
        cursor = conexion.cursor()

        query = """
        INSERT INTO eventos (nombre_evento, categoria, descripcion, entradas_disponibles, localizacion, precio_entrada)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (nombre_evento, categoria, descripcion, entradas_disponibles, localizacion, precio_entrada)

        cursor.execute(query, values)
        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for('crear_evento_form'))  



@app.route('/reserva')
def Reserva():
    return render_template('reserva.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

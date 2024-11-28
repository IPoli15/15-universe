from flask import Flask, render_template, request, current_app, redirect, url_for, flash, jsonify
import requests

PORT = 5000
BACKEND_URL = "http://127.0.0.1:5001"
app = Flask(__name__)
app.secret_key = 'coqui2529'
# Variable para validar si es admin o no,
# app.config es un diccionario especial de flask para almacenar configuraciones de la aplicación,
# estas estan disponibles en toda la aplicacion y son accesibles desde cualquier parte de la misma
app.config['ES_ADMIN'] = False
app.config['SESION_INICIADA'] = False
app.config['ID_USUARIO'] = 0
app.config['NOMBRE_USUARIO'] = ''

@app.route('/')
def index():
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos-recomendados')
        response.raise_for_status()
        eventos = response.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500
    try:
        return render_template('index.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos)

    except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        
        try:
            # Enviar los datos al backend
            response = requests.post('http://localhost:5001/usuarios-password', json={
                'nombre': nombre,
                'password': password
            })
            data = response.json()
            
            if data['success']:
                print('Login successful')
                app.config['NOMBRE_USUARIO'] = nombre
                if data['es_admin']:
                    app.config['ES_ADMIN'] = True
                else:
                    app.config['SESION_INICIADA'] = True
                return redirect(url_for('index'))
            else:
                print('Invalid credentials')
                return redirect(url_for('login'))
        except Exception as e:
            print(f'An error occurred: {str(e)}')
            return redirect(url_for('login'))
    
    return render_template('login.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'])

@app.route('/logout')
def logout():
    app.config['SESION_INICIADA'] = False
    app.config['ES_ADMIN'] = False
    app.config['ID_USUARIO'] = 0
    app.config['NOMBRE_USUARIO'] = ''
    return redirect(url_for('index'))

@app.route('/pago', methods=['GET', 'POST'])
def Pago():
    nombre_usuario = app.config.get('NOMBRE_USUARIO', '')
    id_evento_deseado = request.args.get('id_evento_deseado', None)

    if request.method == 'POST':
        nombre = request.form['nombre']
        id_evento = request.form['id_evento']
        cant_tickets = request.form['cant_tickets']
        
        try:
            # Enviar los datos al backend
            response = requests.post('http://localhost:5001/crear-reserva', json={
                'nombre': nombre,
                'id_evento': id_evento,
                'cant_tickets': cant_tickets
            })
            data = response.json()
            print(data)
            
            if response.status_code == 201 and data['success']:
                id_reserva = data.get("id_reserva")
                flash(f'Pago exitoso. Id de la reserva: {id_reserva}', 'success')
                return render_template('pago_confirmado.html', id_reserva=id_reserva, es_admin=app.config['ES_ADMIN'],
                            sesion_iniciada=app.config['SESION_INICIADA'])
            else:
                flash('Error en el pago: ' + data.get('message', 'Unknown error'))
                return redirect(url_for('Pago'))
        except Exception as e:
            print(f'An error occurred: {str(e)}')
            return redirect(url_for('error'))
    
    # Si el método es GET, renderizar la plantilla de pago
    return render_template('pago.html', es_admin=app.config['ES_ADMIN'],
                            sesion_iniciada=app.config['SESION_INICIADA'],
                            nombre_usuario=nombre_usuario ,
                            id_evento_deseado=id_evento_deseado)


@app.route('/conciertos')
def conciertos():
    nombre_categoria = 'Musica'
    descripcion_categoria = '¡Disfruta de la mejor musica en BA!'
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos/'+nombre_categoria)
        response.raise_for_status()
        eventos = response.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500
    
    try:
        return render_template('conciertos.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos, nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria )

    except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500





@app.route('/cultura_jp')
def cultura_jp():
    nombre_categoria = 'Cultura Japonesa'
    descripcion_categoria = '¡Visita todos los eventos relacionados al mundo de la Cultura Japonesa!'
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos/'+nombre_categoria)
        response.raise_for_status()
        eventos = response.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500
    
    try:
        return render_template('cultura_jp.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos, nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria )

    except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500

    return render_template('cultura_jp.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos, nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria )

@app.route('/fiestas')
def fiestas():
    nombre_categoria = 'Fiestas'
    descripcion_categoria = '¡Las mejores fiestas estan aquí!'
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos/'+nombre_categoria)
        response.raise_for_status()
        eventos = response.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500
    
    try:
        return render_template('fiestas.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos, nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria )

    except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500

@app.route('/eSports')
def esports():
    nombre_categoria = 'eSports'
    descripcion_categoria = '¡Los Torneos de eSports mas relevantes el país!'
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos/'+nombre_categoria)
        response.raise_for_status()
        eventos = response.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500
    
    try:
        return render_template('eSports.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos, nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria )

    except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500

@app.route('/error')
def error():
    return render_template('error.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'])


@app.route('/reserva', methods=["GET", "POST"])
def reserva():
    if request.method == "POST":
        id_reserva = request.form.get('id_reserva')

        if not id_reserva:
            return "Falta el ID de reserva", 400

        try:
            # Consultar reserva en el backend
            response = requests.get(f'http://127.0.0.1:5001/consultar-reserva/{id_reserva}')
            response.raise_for_status()
            datos_reserva = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return render_template('reserva.html', error="Este ID no se encuentra registrado")

        if not datos_reserva:
            return render_template('reserva.html', error="No se encontraron reservas con ese número de ID.")

        # Renderizar plantilla con los datos de la reserva
        # Aquí estamos pasando correctamente los datos del JSON a la plantilla.
        return render_template('tu-reserva.html', **datos_reserva)

    return render_template('reserva.html', es_admin=app.config.get('ES_ADMIN', False), sesion_iniciada=app.config.get('SESION_INICIADA', False))



@app.route('/futbol')
def Futbol():
    nombre_categoria = 'Futbol'
    descripcion_categoria = '¡Disfruta de los mejores eventos del mundo del futbol!'
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos/'+nombre_categoria)
        response.raise_for_status()
        eventos = response.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500
    
    try:
        return render_template('futbol.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos, nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria )

        
    except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500

@app.route('/stand-up')
def Stand_up():
    nombre_categoria = 'Stand Up'
    descripcion_categoria = '¡Disfruta de los MEJORES Shows de Stand Up!'
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos/'+nombre_categoria)
        response.raise_for_status()
        eventos = response.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500
    
    try:
        return render_template('stand_up.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos, nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria )

        
    except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500
    
@app.route('/teatro')
def Teatro():
    nombre_categoria = 'Teatro'
    descripcion_categoria = '¡Disfruta de las mejores obras de Teatro del pais!'
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos/'+nombre_categoria)
        response.raise_for_status()
        eventos = response.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500
    
    try:
        return render_template('Teatro.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'], eventos=eventos, nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria )
    except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500

# - -- - --crear evento----
@app.route('/crear_evento', methods=['GET', 'POST'])
def crear_evento():
    if request.method == 'POST':
        data = {
            'nombre_evento': request.form['nombre_evento'],
            'categoria': request.form['categoria'],
            'descripcion': request.form['descripcion'],
            'entradas_disponibles': request.form['entradas_disponibles'],
            'localizacion': request.form['localizacion'],
            'precio_entrada': request.form['precio_entrada']
        }
        
        response = requests.post(f"{BACKEND_URL}/api/crear_evento", json=data)

        if response.status_code == 201:
            flash('Evento creado con éxito.', 'success')
            return redirect('/crear_evento')
        else:
            flash(response.json().get('error', 'Error desconocido al crear el evento.'), 'danger')

    return render_template('crear_evento.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'])


@app.route('/descripcion-evento/<id_evento>')
def Descripcion_evento(id_evento):
    try:
            response = requests.get('http://127.0.0.1:5001/consultar-eventos/'+id_evento)
            response.raise_for_status()
            datos_evento = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        datos_evento = []
        return str(e), 500
    
    try:
        if datos_evento:
                
            id_evento=datos_evento['id_evento']
            nombre_evento=datos_evento['nombre_evento']
            categoria=datos_evento['categoria']
            descripcion=datos_evento['descripcion']
            entradas_disponibles=datos_evento['entradas_disponibles']
            localizacion=datos_evento['localizacion']
            precio_entrada=datos_evento['precio_entrada']
            fecha_hora=datos_evento['fecha_hora']
            entradas_totales=datos_evento['entradas_totales']
            imagen_url=datos_evento['imagen_url']

            return render_template(
            'descripcion_evento.html', es_admin=app.config['ES_ADMIN'], sesion_iniciada=app.config['SESION_INICIADA'],  id_evento=id_evento,
                                nombre_evento=nombre_evento, 
                                categoria=categoria, 
                                descripcion=descripcion, 
                                entradas_disponibles=entradas_disponibles,
                                localizacion=localizacion,
                                precio_entrada=precio_entrada,
                                fecha_hora=fecha_hora,
                                entradas_totales=entradas_totales,
                                imagen_url=imagen_url
                                )
            
        else:
            return "No se encontraron eventos", 404

    except Exception as e:
        print(f'Unexpected error: {e}')
        return str(e), 500

@app.route('/busqueda-eventos')
def busqueda_eventos():
    nombre_evento = request.args.get('fname')
    try:
        response = requests.get('http://127.0.0.1:5001/consultar-eventos')
        response.raise_for_status()
        eventos = response.json()
        print(eventos)
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f'Error: {e}')
        return str(e), 500    
    try:
        eventos_filtrados = []
        if nombre_evento:
            eventos_filtrados = []
            for evento in eventos: 
                if nombre_evento.lower() in evento.get('nombre_evento', '').lower():
                    eventos_filtrados.append(evento)
        else:
            eventos_filtrados = eventos
        
        if not eventos_filtrados:
            return "No se encontraron eventos que coincidan con la búsqueda."
    except Exception as e:
        current_app.logger.error(f'Unexpected error: {e}')
        return str(e), 500

    return render_template('eSports.html', 
                        es_admin=app.config['ES_ADMIN'], 
                        sesion_iniciada=app.config['SESION_INICIADA'], 
                        eventos=eventos_filtrados)

from flask import redirect, url_for, flash, session

@app.route('/verificar_sesion/<int:id_evento_deseado>')
def verificar_sesion(id_evento_deseado):
    if not app.config['SESION_INICIADA'] and not app.config["ES_ADMIN"]:
        flash('⚠ Debes iniciar sesión antes de reservar una entrada.',"login_incorrecto")
        return redirect(url_for('login'))
    return redirect(url_for('Pago', id_evento_deseado=id_evento_deseado))

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Página no encontrada"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=PORT)

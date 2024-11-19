from flask import Flask, render_template, request, current_app
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

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

@app.route('/reserva', methods=["GET", "POST"])
def Reserva():
    if request.method == "POST":
        id_reserva = request.form.get('id_reserva')

        try:
            response = requests.get('http://127.0.0.1:5001/consultar-reserva/'+id_reserva)
            response.raise_for_status()
            datos_reserva = response.json()
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f'Error: {e}')
            return str(e), 500
    
        try:
            if datos_reserva:

                nombre_usuario=datos_reserva['nombre_usuario']
                nombre_evento=datos_reserva['nombre_evento']
                precio_entrada=datos_reserva['precio_entradda']
                id_reserva=datos_reserva['id_reserva']
                cant_tickets=datos_reserva['cant_tickets']

                return render_template(
                'tu-reserva.html',  id_reserva=id_reserva,
                                    cant_tickets=cant_tickets, 
                                    nombre_usuario=nombre_usuario, 
                                    nombre_evento=nombre_evento, 
                                    precio_entrada=precio_entrada,
                                    total=precio_entrada*cant_tickets)
            
            else:
                return "No se encontraron reservas con es numero de ID", 404

        except Exception as e:
            current_app.logger.error(f'Unexpected error: {e}')
            return str(e), 500
    return render_template('reserva.html')

@app.route('/pago')
def Pago():
    return render_template('pago.html')

@app.route('/futbol')
def Futbol():
    nombre_categoria='Futbol'
    descripcion_categoria = 'Disfruta de los mejores eventos de Futbol'
    eventos=[{'nombre':"Visita al museo de Boca Juniors", 'descripcion':'Disfruta una visita al museo de uno de los mejores equipos de Argentina y America'},
             {'nombre':"Visita al museo de Boca Juniors", 'descripcion':'Disfruta una visita al museo de uno de los mejores equipos de Argentina y America'},
             {'nombre':"Visita al museo de Boca Juniors", 'descripcion':'Disfruta una visita al museo de uno de los mejores equipos de Argentina y America'},
             {'nombre':"Visita al museo de Boca Juniors", 'descripcion':'Disfruta una visita al museo de uno de los mejores equipos de Argentina y America'}]

    return render_template('futbol.html', nombre_categoria=nombre_categoria,descripcion_categoria=descripcion_categoria, eventos=eventos )

@app.route('/stand-up')
def Stand_up():
    return render_template('stand_up.html')

@app.route('/teatro')
def Teatro():
    return render_template('Teatro.html')


if __name__ == '__main__':
    app.run(debug=True)
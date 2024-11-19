from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/crear_evento')
def crear_evento():
    return render_template('crear_evento.html')

@app.route('/musica')
def musica():
    return render_template('musica.html')

@app.route('/cultura_jp')
def cultura_jp():
    return render_template('cultura_jp.html')

@app.route('/Fiesta')
def Fiesta():
    return render_template('Fiesta.html')

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

if __name__ == '__main__':
    app.run(debug=True)

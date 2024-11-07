from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pago.html')

@app.route('/futbol')
def Futbol():
    return render_template('futbol.html')

@app.route('/reserva')
def Reserva():
    return render_template('reserva.html')

@app.route('/pago')
def Pago():
    return render_template('pago.html')

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

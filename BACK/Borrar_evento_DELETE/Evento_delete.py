from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

engine = create_engine("mysql+mysqlconnector://root:tuclave@localhost:3306/universe")

def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()
    return result

@app.route('/eliminar-evento/<int:id_evento>', methods=['DELETE'])
def eliminar_evento(id_evento):
    try:      
        query_reservas_evento = "SELECT COUNT(*) FROM query_tabla_reservas WHERE id_evento = :id_evento"
        result_reservas = run_query(query_reservas_evento, {'id_evento': id_evento}).fetchone()

        if result_reservas[0] > 0:
        
            query_eliminar_reservas = "DELETE FROM query_tabla_reservas WHERE id_evento = :id_evento"
            run_query(query_eliminar_reservas, {'id_evento': id_evento})
        
        query_eliminar_evento = "DELETE FROM query_tabla_eventos WHERE id_evento = :id_evento"
        result = run_query(query_eliminar_evento, {'id_evento': id_evento})

       
        if result.rowcount == 0:
            return jsonify({'error': 'No se encontró un evento con este ID'}), 404

        return jsonify({'mensaje': f'El evento ID {id_evento} fue eliminado junto con sus reservas'}), 200
    
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

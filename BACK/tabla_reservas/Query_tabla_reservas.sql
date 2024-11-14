USE universe;

CREATE TABLE reservas (
    id_usuarios INT,
    id_evento INT,
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    cant_tickets INT,
    FOREIGN KEY (id_usuarios) REFERENCES usuarios(id_usuarios),
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);

INSERT INTO reservas (cant_tickets)

VALUES
(20);

SELECT * FROM reservas;
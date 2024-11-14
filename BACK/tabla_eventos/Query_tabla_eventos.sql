USE universe;

CREATE TABLE IF NOT EXISTS eventos (
    id_evento INT PRIMARY KEY AUTO_INCREMENT,
    nombre_evento VARCHAR(50) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    descripcion VARCHAR(150) NOT NULL,
    entradas_disponibles INT NOT NULL,
    localizacion VARCHAR(50) NOT NULL,
    precio_entrada DECIMAL(5,2) NOT NULL
);

INSERT INTO eventos (nombre_evento, categoria, descripcion, entradas_disponibles, localizacion, precio_entrada)

VALUES
('concierto', 'musica', 'concierto de rock', 100, 'Av directorio 1453', 20.00);

SELECT * FROM eventos;
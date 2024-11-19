USE universe;

---------------------------------------------- USUARIOS

-- Query Create de Tabla usuarios:
CREATE TABLE IF NOT EXISTS usuarios (
  id_usuario  INT AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(50),
  password varchar(50)
);

-- Query Insert de Tabla usuarios:
INSERT INTO usuarios (nombre, password)
VALUES
('alejandro' , '111'),
('henry' , '441'),
('blas' , '123'),
('yohara' , '555'),
('nacho' , '789'),
('santiago' , '631'),
('ruy' , '911');

-- Query Select de Tabla usuarios:
SELECT * FROM usuarios;

---------------------------------------------- EVENTOS

-- Query Create de Tabla eventos:
CREATE TABLE IF NOT EXISTS eventos (
    id_evento INT PRIMARY KEY AUTO_INCREMENT,
    nombre_evento VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    entradas_disponibles INT NOT NULL,
    localizacion VARCHAR(50) NOT NULL,
    precio_entrada INT NOT NULL
);

-- Query Insert de Tabla eventos:
INSERT INTO eventos (nombre_evento, categoria, descripcion, entradas_disponibles, localizacion, precio_entrada)
VALUES
('visita museo de boca juniors', 'futbol', 'conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 100, 'Av directorio 1453', 5000),
('concierto camilo', 'musica', 'Concierto de camilo echeverry', 300, 'Movistar arena', 20000),
('fiesta grim', 'fiestas', 'Sexta edicion tematica HALLOWEEN', 50, 'Sarmiento 1752', 7000),
('cascanueces', 'teatro', 'evento en el teatro colon', 250, 'tucuman 1171', 9000),
('cultura japonesa', 'cultura japonesa', 'evento de cultura japonesa', 20, 'jardin japones', 4000),
('worlds 2024', 'esports', 'campeonato mundial de League of Legends', 800, 'Av Bartolome Mitre 219', 31000),
('show de stand up', 'stand up', 'el show de Franco Escamilla', 400, 'Teatro Gran Rex', 11000);

-- Query Select de Tabla eventos:
SELECT * FROM eventos;
---------------------------------------------- RESERVAS

-- Query Create de Tabla reservas:
CREATE TABLE reservas (
    id_usuario INT,
    id_evento INT,
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    cant_tickets INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);

-- Query Insert de Tabla reservas:
INSERT INTO reservas (id_usuario, id_evento, cant_tickets)
VALUES
(1, 1, 20),
(2, 2, 40);

-- Query Select de Tabla reservas:
SELECT * FROM reservas;
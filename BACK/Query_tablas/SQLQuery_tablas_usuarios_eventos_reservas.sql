CREATE DATABASE IF NOT EXISTS universe;

USE universe;

CREATE TABLE IF NOT EXISTS usuarios (
  id_usuario  INT AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(50),
  password varchar(50),
  es_admin BOOLEAN
);

INSERT INTO usuarios (nombre, password, es_admin)
VALUES
('ADMIN' , 'ADMIN', 1),
('USER' , 'USER', 0);

SELECT * FROM usuarios;

CREATE TABLE IF NOT EXISTS eventos (
    id_evento INT PRIMARY KEY AUTO_INCREMENT,
    nombre_evento VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    descripcion TEXT NOT NULL,
    entradas_totales INT NOT NULL,
    entradas_disponibles INT NOT NULL,
    fecha_hora VARCHAR(50) NOT NULL,
    localizacion VARCHAR(200) NOT NULL,
    es_recomendacion BOOLEAN,
    precio_entrada INT NOT NULL
);

INSERT INTO eventos (nombre_evento, categoria, descripcion, entradas_totales, entradas_disponibles, fecha_hora, localizacion, es_recomendacion, precio_entrada)
VALUES
('Superclásico: Boca Juniors vs River Plate', 'futbol', 'El partido más esperado del fútbol argentino. Boca Juniors recibe a River Plate en la Bombonera para una nueva edición del Superclásico. Disfruta del ambiente único y la pasión desbordante de este histórico enfrentamiento entre los dos equipos más grandes de Argentina.', 50000, 15000, '30 de Noviembre, 17:00 hs', 'Estadio Alberto J. Armando (La Bombonera), Brandsen 805, Buenos Aires, Argentina', 1, 15000),
('Final de la Copa Argentina: Vélez Sarsfield vs Central Córdoba', 'futbol', 'Los equipos más destacados de la Copa de la Liga se enfrentan en la gran final. Vélez Sarsfield se mide contra Central Córdoba en un duelo que promete mucha emoción, goles y una definición al límite.', 40000, 20000, '5 de Diciembre, 20:00 hs', 'Estadio Mario Alberto Kempes, Ramón Cárcano, Córdoba', 0, 10000),
('Fútbol Femenino: Independiente vs San Lorenzo', 'futbol', 'Disfruta de un emocionante encuentro de fútbol femenino entre dos de los equipos más importantes de Argentina. Independiente enfrenta a San Lorenzo en un clásico lleno de jugadas de alto nivel y mucho entusiasmo.', 35000, 10000, '10 de Diciembre, 15:00 hs', 'Estadio Libertadores de América - Ricardo Enrique Bochini, Ricardo Enrique Bochini 751, Avellaneda, Provincia de Buenos Aires', 0, 5000),
('Partido Internacional: Argentina vs Uruguay', 'futbol', 'El clásico del Río de la Plata se juega en Buenos Aires. La selección argentina se enfrenta a su histórico rival, Uruguay, en un partido lleno de historia, emoción y talento futbolístico. Perfecto para los fanáticos de la selección y del fútbol sudamericano.', 80000, 60000, '10 de Diciembre, 21:00 hs', 'Estadio Monumental, Av. Figueroa Alcorta 7597, Buenos Aires, Argentina', 0, 50000),
('Concierto de Rock: La Renga en Vivo', 'musica', 'La legendaria banda de rock argentino La Renga se presenta en Buenos Aires para ofrecer un show inolvidable. Con su característico estilo de rock pesado y letras intensas, promete una noche llena de energía y emociones. ¡No te lo pierdas!', 40000, 10000, '15 de diciembre de 2024, 21:00 hs', 'Estadio de Ferro, Av. Avellaneda 1240, Buenos Aires, Argentina', 1, 10000),
('Festival de Música Electrónica: Ultra Buenos Aires 2024', 'musica', 'El festival de música electrónica más grande de Argentina regresa a Buenos Aires. Con los DJs más destacados del mundo y un ambiente único, Ultra Buenos Aires ofrecerá shows espectaculares, luces, y música de alto nivel para los amantes del EDM y la cultura electrónica.', 65000, 30000, '7 de diciembre de 2024, 14:00 hs', 'Campo de Polo, Av. del Libertador 4101, Buenos Aires, Argentina', 0, 5000),
('Festival de Música Latinoamericana: Sonidos del Mundo', 'musica', 'Un viaje musical por América Latina, donde artistas de diferentes países compartirán su música tradicional y moderna. Con presentaciones de artistas de Colombia, México, Brasil y Argentina, el festival Sonidos del Mundo promete un día lleno de ritmos, colores y culturas diversas.', 20000, 12000, '21 de Diciembre, 12:00 hs', 'Tecnópolis, Av. de los Constituyentes 2000, Villa Martelli, Buenos Aires, Argentina', 0, 5000),
('Concierto de Tango: Astor Piazzolla 100 años', 'musica', 'En conmemoración al centenario de Astor Piazzolla, este concierto de tango será una celebración de su legado musical. Una orquesta especialmente formada interpretará algunas de sus composiciones más icónicas, como Libertango y Adiós Nonino. Un evento imperdible para los amantes del tango y la música clásica argentina.', 2000, 1000, '10 de diciembre de 2024, 20:00 hs', 'Teatro Colón, Tucumán 1171, Buenos Aires, Argentina', 0, 2500),
('Visita al Museo de Boca Juniors', 'fiestas', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 1, 5000),
('Visita al Museo de Boca Juniors', 'fiestas', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'fiestas', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'fiestas', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'teatro', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 1, 5000),
('Visita al Museo de Boca Juniors', 'teatro', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'teatro', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'teatro', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'cultura japonesa', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 1, 5000),
('Visita al Museo de Boca Juniors', 'cultura japonesa', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'cultura japonesa', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'cultura japonesa', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'esports', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 1, 5000),
('Visita al Museo de Boca Juniors', 'esports', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'esports', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'esports', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'stand up', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 1, 5000),
('Visita al Museo de Boca Juniors', 'stand up', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'stand up', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000),
('Visita al Museo de Boca Juniors', 'stand up', 'Conoce el museo de Boca Juniors con la exposicion de sus trofeos mas importantes', 300, 100, '30/11, 10:00 hs', 'Brandsen 805', 0, 5000);


SELECT * FROM eventos;

CREATE TABLE reservas (
    id_usuario INT,
    id_evento INT,
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    cant_tickets INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);

INSERT INTO reservas (id_usuario, id_evento, cant_tickets)
VALUES
(1, 1, 20),
(2, 2, 40);


SELECT * FROM reservas;


-- DROP DATABASE universe;
DROP TABLE reservas;
DROP TABLE eventos;
DROP TABLE usuarios;
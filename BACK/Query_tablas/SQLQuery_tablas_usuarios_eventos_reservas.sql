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
    precio_entrada INT NOT NULL,
    imagen_url TEXT
);

INSERT INTO eventos (nombre_evento, categoria, descripcion, entradas_totales, entradas_disponibles, fecha_hora, localizacion, es_recomendacion, precio_entrada, imagen_url)
VALUES
('Superclásico: Boca Juniors vs River Plate', 'futbol', 'El partido más esperado del fútbol argentino. Boca Juniors recibe a River Plate en la Bombonera para una nueva edición del Superclásico. Disfruta del ambiente único y la pasión desbordante de este histórico enfrentamiento entre los dos equipos más grandes de Argentina.', 50000, 15000, '30 de Noviembre, 17:00 hs', 'Estadio Alberto J. Armando (La Bombonera), Brandsen 805, Buenos Aires, Argentina', 1, 15000,'https://mas10.ar/wp-content/uploads/2023/05/boca-river_862x485.jpg'),
('Final de la Copa Argentina: Vélez Sarsfield vs Central Córdoba', 'futbol', 'Los equipos más destacados de la Copa de la Liga se enfrentan en la gran final. Vélez Sarsfield se mide contra Central Córdoba en un duelo que promete mucha emoción, goles y una definición al límite.', 40000, 20000, '5 de Diciembre, 20:00 hs', 'Estadio Mario Alberto Kempes, Ramón Cárcano, Córdoba', 0, 10000,'https://www.apuestas-argentina.com/wp-content/uploads/2024/07/Central-Cordoba-vs-Velez-pronostico-1024x583.webp'),
('Fútbol Femenino: Independiente vs San Lorenzo', 'futbol', 'Disfruta de un emocionante encuentro de fútbol femenino entre dos de los equipos más importantes de Argentina. Independiente enfrenta a San Lorenzo en un clásico lleno de jugadas de alto nivel y mucho entusiasmo.', 35000, 10000, '10 de Diciembre, 15:00 hs', 'Estadio Libertadores de América - Ricardo Enrique Bochini, Ricardo Enrique Bochini 751, Avellaneda, Provincia de Buenos Aires', 0, 5000,'https://i.ytimg.com/vi/PTDFpaoXyGo/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCWdt5gNHq1QP7kGrizW8E2eGGAWw'),
('Partido Internacional: Argentina vs Uruguay', 'futbol', 'El clásico del Río de la Plata se juega en Buenos Aires. La selección argentina se enfrenta a su histórico rival, Uruguay, en un partido lleno de historia, emoción y talento futbolístico. Perfecto para los fanáticos de la selección y del fútbol sudamericano.', 80000, 60000, '10 de Diciembre, 21:00 hs', 'Estadio Monumental, Av. Figueroa Alcorta 7597, Buenos Aires, Argentina', 0, 50000,'https://e00-mx-marca.uecdn.es/mx/assets/multimedia/imagenes/2023/11/16/17001713448974.jpg'),
('Concierto de Rock: La Renga en Vivo', 'musica', 'La legendaria banda de rock argentino La Renga se presenta en Buenos Aires para ofrecer un show inolvidable. Con su característico estilo de rock pesado y letras intensas, promete una noche llena de energía y emociones. ¡No te lo pierdas!', 40000, 10000, '15 de diciembre de 2024, 21:00 hs', 'Estadio de Ferro, Av. Avellaneda 1240, Buenos Aires, Argentina', 1, 10000,'https://www.laizquierdadiario.com/IMG/logo/lid_-_la_renga_creedito_fb_la_renga_oficial_.jpg?1705093586'),
('Festival de Música Electrónica: Ultra Buenos Aires 2024', 'musica', 'El festival de música electrónica más grande de Argentina regresa a Buenos Aires. Con los DJs más destacados del mundo y un ambiente único, Ultra Buenos Aires ofrecerá shows espectaculares, luces, y música de alto nivel para los amantes del EDM y la cultura electrónica.', 65000, 30000, '7 de diciembre de 2024, 14:00 hs', 'Campo de Polo, Av. del Libertador 4101, Buenos Aires, Argentina', 0, 5000,'https://www.ciudad.com.ar/resizer/v2/el-evento-se-llevara-a-cabo-del-18-al-19-de-abril-de-2025-en-el-emblematico-parque-de-la-ciudad-X2UXOIOYCBCQZEZCESGAVPO3OM.jpg?auth=7b238634a311313b027dfb6949713ae94583346723b0497f8d48166d2e6ee879&width=767'),
('Festival de Música Latinoamericana: Sonidos del Mundo', 'musica', 'Un viaje musical por América Latina, donde artistas de diferentes países compartirán su música tradicional y moderna. Con presentaciones de artistas de Colombia, México, Brasil y Argentina, el festival Sonidos del Mundo promete un día lleno de ritmos, colores y culturas diversas.', 20000, 12000, '21 de Diciembre, 12:00 hs', 'Tecnópolis, Av. de los Constituyentes 2000, Villa Martelli, Buenos Aires, Argentina', 0, 5000,'https://experienciajoven.com/wp-content/uploads/2023/01/Los-mejores-festivales-de-musica-del-mundo-2.jpg'),
('Concierto de Tango: Astor Piazzolla 100 años', 'musica', 'En conmemoración al centenario de Astor Piazzolla, este concierto de tango será una celebración de su legado musical. Una orquesta especialmente formada interpretará algunas de sus composiciones más icónicas, como Libertango y Adiós Nonino. Un evento imperdible para los amantes del tango y la música clásica argentina.', 2000, 1000, '10 de diciembre de 2024, 20:00 hs', 'Teatro Colón, Tucumán 1171, Buenos Aires, Argentina', 0, 2500,'https://www.arte-online.net/var/arte_online_net/storage/images/arte-online/agenda/exposiciones_muestras/piazzolla-100/893574-1-esl-AR/Piazzolla-100_nota.png'),
('FIESTA BRESH', 'fiestas', 'La fiesta de la juventud de Buenos Aires. La Bresh es una de las fiestas más populares entre los jóvenes, con una mezcla de reggaeton, trap, y música urbana, ¡y es un evento que no te podés perder!', 6000, 2500, '9 de Diciembre, 00:00 hs', 'La Trastienda, Balcarce 460, San Telmo, Buenos Aires, Argentina', 1, 4000, 'https://ganaconacqua.com.ar/wp-content/uploads/2024/01/bresh-en-mar-del-plata.jpg'),
('Fiesta Flow', 'fiestas', 'La fiesta donde el reggaeton, trap y música urbana invaden la pista de baile. Ven a disfrutar de una noche inolvidable con los mejores DJs del género. ¡No te la podés perder!', 5000, 2000, '6 de Diciembre, 00:00 hs', 'Café Berlín, Humboldt 189, Villa Crespo, Buenos Aires, Argentina', 0, 2000, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiVhJ_Rt8CSVGtKvTJdiu_ug0u9fYcSBohZQ&s'),
('La Fiesta de la Cumbia y el Reggaeton', 'fiestas', 'Para los fanáticos de la cumbia, reggaeton y música latina, esta fiesta es el lugar perfecto para bailar hasta el amanecer. Ven a disfrutar de la mejor cumbia y reggaeton en un ambiente único.', 3500, 1500, '3 de Diciembre, 00:00 hs', 'La Peña del Colorado, Rodríguez Peña 1250, San Telmo, Buenos Aires, Argentina', 0, 3000, 'https://i.ytimg.com/vi/UNIC7z882bY/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLA8wDaVPokoCoDZEcbzvFR7sbUd5Q'),
('El Circo de los Horrores', 'teatro', 'El Circo de los Horrores es un show único donde se mezcla el teatro con el circo y el horror. Espectáculos impactantes que desafían los límites de la mente humana, un verdadero despliegue de emoción y adrenalina.', 3000, 1000, '10 de Diciembre, 21:00 hs', 'Teatro Liceo, Av. Rivadavia 1499, CABA, Buenos Aires, Argentina', 1, 1500, 'https://teatromadrid.com/wp-content/uploads/2023/07/TEATRO_MADRID-Requiem-1-1100x733.jpg'),
('La Casa de Bernarda Alba', 'teatro', 'La obra de Federico García Lorca, "La Casa de Bernarda Alba", es un drama que explora la represión y el autoritarismo en una familia de mujeres. Un clásico del teatro español, de gran intensidad emocional.', 2000, 800, '14 de Diciembre, 20:30 hs', 'Teatro San Martín, Av. Corrientes 1530, CABA, Buenos Aires, Argentina', 0, 1200, 'https://livepkassets.pechakucha.com/slides/e2bf7542-f138-4bee-83f1-f7f8976ed7c0/padblack_noborder_1600x900/slide_20_1614114932065.jpg'),
('Medea', 'teatro', 'Medea es una tragedia griega que explora temas como la venganza, la justicia y el amor. Esta versión contemporánea de la obra de Eurípides promete una puesta en escena desgarradora y llena de emoción.', 1500, 500, '16 de Diciembre, 20:00 hs', 'Teatro Colon, Cerrito 628, CABA, Buenos Aires, Argentina', 0, 1800, 'https://i0.wp.com/academiadesanromualdo.com/wp-content/uploads/2023/03/medea09.jpg?fit=1280%2C720&ssl=1'),
('Un Dios Salvaje', 'teatro', 'Una comedia negra que explora los límites del civismo y la moralidad en una reunión entre dos parejas que se enfrentan a la violencia latente detrás de las apariencias. Un teatro de gran tensión y humor ácido.', 2500, 1000, '18 de Diciembre, 21:30 hs', 'Teatro Maipo, Esmeralda 443, CABA, Buenos Aires, Argentina', 0, 1000, 'https://img.alternativateatral.com/scripts/es/fotos/obras/resumen/000038716.jpg'),
('Festival de Cine Japonés', 'cultura japonesa', 'El Festival de Cine Japonés es el evento ideal para los amantes del cine asiático. Disfruta de una selección de las mejores películas japonesas actuales y clásicas, que exploran la riqueza cultural y el cine de Japón.', 2000, 800, '4 de Diciembre, 19:00 hs', 'Cine Gaumont, Av. Rivadavia 1635, CABA, Buenos Aires, Argentina', 1, 600, 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/XRCVQTNU5RDH3O2EOENYKFG25I.jpg'),
('Exposición de Arte Japonés', 'cultura japonesa', 'Una exposición única de arte japonés donde podrás disfrutar de las obras de artistas contemporáneos japoneses, así como una sección dedicada a la tradición artística ancestral del país. Una oportunidad para explorar el arte de Japón.', 1500, 600, '8 de Diciembre, 18:00 hs', 'Museo Nacional de Bellas Artes, Av. del Libertador 1473, CABA, Buenos Aires, Argentina', 0, 500, 'https://images.pagina12.com.ar/styles/focal_16_9_960x540/public/2023-01/691265-museo-20nacional-20de-20arte-20oriental-0.jpg?h=29234840&itok=pHSnSRnv'),
('Festival del Hanami', 'cultura japonesa', 'Celebra el Hanami, la tradicional fiesta japonesa de observación de los cerezos en flor. En este festival podrás disfrutar de actividades culturales, danzas, música y una exhibición de sakura, el símbolo nacional de Japón.', 3000, 1200, '7 de Diciembre, 12:00 hs', 'Parque Tres de Febrero (Rosedal), Av. Infanta Isabel, CABA, Buenos Aires, Argentina', 0, 200, 'https://www.clarin.com/2016/03/18/BJeXzToYEx_720x0.jpg'),
('Taller de Origami y Caligrafía Japonesa', 'cultura japonesa', 'Un taller interactivo donde podrás aprender el arte del origami (plegado de papel) y la caligrafía japonesa. Un evento para todos los interesados en la cultura japonesa y sus tradiciones más artísticas.', 500, 200, '10 de Diciembre, 15:00 hs', 'Parque Tres de Febrero (Rosedal), Av. Infanta Isabel, CABA, Buenos Aires, Argentina', 0, 500, 'https://nichiagakuin.edu.ar/ngf/images/t_2016/clip_image008.jpg'),
('Liga Latinoamérica de League of Legends', 'esports', 'La Liga Latinoamérica (LLA) es la principal competencia de League of Legends en América Latina. Los mejores equipos de la región se enfrentan en un torneo de alta competencia y emoción. Un evento imperdible para los fanáticos del LoL.', 5000, 2000, '15 de Diciembre, 18:00 hs', 'Arena de e-sports, Av. Córdoba 1234, CABA, Buenos Aires, Argentina', 1, 1000, 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/IVZZCTSBSRAYPDZVEJXP2SHBTA.jpg'),
('Torneo de Valorant: Copa Argentina', 'esports', 'Un torneo competitivo de Valorant en el que los mejores jugadores y equipos de Argentina luchan por el campeonato nacional. ¡Ven a ser parte de la emoción mientras los equipos de e-sports compiten por la gloria!', 3000, 1200, '20 de Diciembre, 17:00 hs', 'Centro de Convenciones de Buenos Aires, Av. Figueroa Alcorta 2000, CABA, Buenos Aires, Argentina', 0, 800, 'https://www.telefonica.com.ar/wp-content/uploads/sites/12/2023/07/Copa-Movistar-Fibra.jpg?w=1224&h=673&crop=1'),
('FIFA 24: Torneo Internacional', 'esports', 'Participa en uno de los torneos de FIFA más prestigiosos, donde jugadores de todo el mundo se enfrentan en intensas rondas para conseguir el título. ¡Demuestra que eres el mejor en el simulador de fútbol más famoso del mundo!', 1500, 600, '22 de Diciembre, 19:30 hs', 'Espacio e-sports, Av. de Mayo 1400, CABA, Buenos Aires, Argentina', 0, 700, 'https://phantom-marca.unidadeditorial.es/16534a711499d3f65810a95abb971c77/resize/828/f/jpg/assets/multimedia/imagenes/2024/02/05/17071550474357.jpg'),
('The International Dota 2: Fase de Clasificación', 'esports', 'Un evento clave para los fanáticos de Dota 2, donde los equipos se enfrentan en la fase clasificatoria de The International, el torneo de e-sports más grande de Dota 2. ¡Ven a ver la acción en vivo y a apoyar a tu equipo favorito!', 4000, 1500, '25 de Diciembre, 14:00 hs', 'Club e-sports Arena, Av. Santa Fe 3500, CABA, Buenos Aires, Argentina', 0, 1000, 'https://larepublica.cronosmedia.glr.pe/original/2021/10/09/6162181c82f48a096e35f1a4.jpg'),
('Carlos Latre: Show en Vivo', 'Stand up', 'Carlos Latre, uno de los comediantes más conocidos de Argentina, se presenta en vivo con un show lleno de humor y personajes. Una noche de risas garantizadas con el estilo único de Latre.', 1000, 500, '5 de Diciembre, 21:00 hs', 'Teatro Gran Rex, Av. Corrientes 857, CABA, Buenos Aires, Argentina', 0, 1500, 'https://cineytele.com/play/wp-content/uploads/2023/04/carlos-latre-oneman-show-cartel.jpg'),
('La Noche de la Comedia', 'Stand up', 'El ciclo de comedia más divertido de Buenos Aires, con diferentes comediantes de la escena local presentando sus mejores monólogos en un show variado y lleno de humor.', 600, 300, '7 de Diciembre, 22:00 hs', 'Café La Humedad, Balcarce 460, CABA, Buenos Aires, Argentina', 0, 500, 'https://imgplateanet.com.ar/imagenes/img/imagenes/425x318/noches-de-comedia-stand-up.jpg'),
('Martín Garabal: Stand-Up Comedy', 'Stand up', 'Martín Garabal, uno de los comediantes más destacados de la escena argentina, regresa con un show de stand-up donde se burla de la vida cotidiana, las redes sociales y más.', 800, 400, '10 de Diciembre, 20:30 hs', 'The Roxy, Av. Juan B. Justo 620, CABA, Buenos Aires, Argentina', 1, 800, 'https://cloudfront-us-east-1.images.arcpublishing.com/grupoclarin/6Q6PUQ4RLFGZHIXNU742GE22JQ.jpeg'),
('Las Pelotas del Stand-Up', 'Stand up', 'Un espectáculo de comedia en donde varios comediantes presentan su mejor material, en una noche llena de risas y diversión. ¡Ideal para pasar una noche divertida con amigos!', 400, 150, '12 de Diciembre, 23:00 hs', 'El Club de la Comedia, Av. Córdoba 4335, CABA, Buenos Aires, Argentina', 0, 600, 'https://standupclubarg.com/wp-content/uploads/2023/09/e7b40f87-155d-4016-b01f-375ba5984fc5-edited.webp');


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
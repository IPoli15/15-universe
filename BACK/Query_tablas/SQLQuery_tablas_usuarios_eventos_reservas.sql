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
    localizacion TEXT NOT NULL,
    es_recomendacion BOOLEAN,
    precio_entrada INT NOT NULL,
    imagen_url TEXT
);

INSERT INTO eventos (nombre_evento, categoria, descripcion, entradas_totales, entradas_disponibles, fecha_hora, localizacion, es_recomendacion, precio_entrada, imagen_url)
VALUES
('Superclásico: Boca Juniors vs River Plate', 'futbol', 'El partido más esperado del fútbol argentino. Boca Juniors recibe a River Plate en la Bombonera para una nueva edición del Superclásico. Disfruta del ambiente único y la pasión desbordante de este histórico enfrentamiento entre los dos equipos más grandes de Argentina.', 50000, 15000, '30 de Noviembre, 17:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.7558016657167!2d-58.367331223481564!3d-34.635610872942976!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95a334b6925e5473%3A0x1ca5b2748858b40d!2sEstadio%20Alberto%20J.%20Armando!5e0!3m2!1ses-419!2sar!4v1732309309997!5m2!1ses-419!2sar", 1, 15000,'https://mas10.ar/wp-content/uploads/2023/05/boca-river_862x485.jpg'),
('Final de la Copa Argentina: Vélez Sarsfield vs Central Córdoba', 'futbol', 'Los equipos más destacados de la Copa de la Liga se enfrentan en la gran final. Vélez Sarsfield se mide contra Central Córdoba en un duelo que promete mucha emoción, goles y una definición al límite.', 40000, 20000, '5 de Diciembre, 20:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3406.6393658349434!2d-64.24872812376971!3d-31.368929574283737!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94329ecc4516ee49%3A0x52b97a2b4d3699bf!2sEstadio%20Mario%20Alberto%20Kempes!5e0!3m2!1ses-419!2sar!4v1732309540811!5m2!1ses-419!2sar", 0, 10000,'https://www.apuestas-argentina.com/wp-content/uploads/2024/07/Central-Cordoba-vs-Velez-pronostico-1024x583.webp'),
('Fútbol Femenino: Independiente vs San Lorenzo', 'futbol', 'Disfruta de un emocionante encuentro de fútbol femenino entre dos de los equipos más importantes de Argentina. Independiente enfrenta a San Lorenzo en un clásico lleno de jugadas de alto nivel y mucho entusiasmo.', 35000, 10000, '10 de Diciembre, 15:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3281.385466796587!2d-58.37391562365507!3d-34.670219672930585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95a3334b39d33bdd%3A0xdb9a534cc563fa7!2sEstadio%20Libertadores%20de%20Am%C3%A9rica%20-%20Ricardo%20Enrique%20Bochini!5e0!3m2!1ses-419!2sar!4v1732309595456!5m2!1ses-419!2sar", 0, 5000,'https://i.ytimg.com/vi/PTDFpaoXyGo/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCWdt5gNHq1QP7kGrizW8E2eGGAWw'),
('Partido Internacional: Argentina vs Uruguay', 'futbol', 'El clásico del Río de la Plata se juega en Buenos Aires. La selección argentina se enfrenta a su histórico rival, Uruguay, en un partido lleno de historia, emoción y talento futbolístico. Perfecto para los fanáticos de la selección y del fútbol sudamericano.', 80000, 60000, '10 de Diciembre, 21:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3286.327858399952!2d-58.452332623659494!3d-34.545253372975395!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb43ae6018ddf%3A0x3d7f60a75bfa308a!2sEstadio%20M%C3%A2s%20Monumental!5e0!3m2!1ses-419!2sar!4v1732310008147!5m2!1ses-419!2sar", 0, 50000,'https://e00-mx-marca.uecdn.es/mx/assets/multimedia/imagenes/2023/11/16/17001713448974.jpg'),
('Concierto de Rock: La Renga en Vivo', 'musica', 'La legendaria banda de rock argentino La Renga se presenta en Buenos Aires para ofrecer un show inolvidable. Con su característico estilo de rock pesado y letras intensas, promete una noche llena de energía y emociones. ¡No te lo pierdas!', 40000, 10000, '15 de diciembre de 2024, 21:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.4297080457914!2d-58.4476404897828!3d-34.61857977398953!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcca3c4529e413%3A0x6d60dd909b07d4c!2sEstadio%20Arquitecto%20Ricardo%20Etcheverri!5e0!3m2!1ses-419!2sar!4v1732310128834!5m2!1ses-419!2sar", 1, 10000,'https://www.laizquierdadiario.com/IMG/logo/lid_-_la_renga_creedito_fb_la_renga_oficial_.jpg?1705093586'),
('Festival de Música Electrónica: Ultra Buenos Aires 2024', 'musica', 'El festival de música electrónica más grande de Argentina regresa a Buenos Aires. Con los DJs más destacados del mundo y un ambiente único, Ultra Buenos Aires ofrecerá shows espectaculares, luces, y música de alto nivel para los amantes del EDM y la cultura electrónica.', 65000, 30000, '7 de diciembre de 2024, 14:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3285.441045673686!2d-58.4320808236587!3d-34.56770517296715!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb51e3d705c27%3A0xf78e9231f8b4d0a!2sCampo%20de%20polo!5e0!3m2!1ses-419!2sar!4v1732310561840!5m2!1ses-419!2sar", 0, 5000,'https://www.ciudad.com.ar/resizer/v2/el-evento-se-llevara-a-cabo-del-18-al-19-de-abril-de-2025-en-el-emblematico-parque-de-la-ciudad-X2UXOIOYCBCQZEZCESGAVPO3OM.jpg?auth=7b238634a311313b027dfb6949713ae94583346723b0497f8d48166d2e6ee879&width=767'),
('Festival de Música Latinoamericana: Sonidos del Mundo', 'musica', 'Un viaje musical por América Latina, donde artistas de diferentes países compartirán su música tradicional y moderna. Con presentaciones de artistas de Colombia, México, Brasil y Argentina, el festival Sonidos del Mundo promete un día lleno de ritmos, colores y culturas diversas.', 20000, 12000, '21 de Diciembre, 12:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3285.7324443354914!2d-58.51418267365906!3d-34.56032912296983!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb750762e0605%3A0x95193eb6582a32c7!2sTecn%C3%B3polis!5e0!3m2!1ses-419!2sar!4v1732310767581!5m2!1ses-419!2sar", 0, 5000,'https://experienciajoven.com/wp-content/uploads/2023/01/Los-mejores-festivales-de-musica-del-mundo-2.jpg'),
('Concierto de Tango: Astor Piazzolla 100 años', 'musica', 'En conmemoración al centenario de Astor Piazzolla, este concierto de tango será una celebración de su legado musical. Una orquesta especialmente formada interpretará algunas de sus composiciones más icónicas, como Libertango y Adiós Nonino. Un evento imperdible para los amantes del tango y la música clásica argentina.', 2000, 1000, '10 de diciembre de 2024, 20:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.1206523100122!2d-58.386110823657454!3d-34.60111047295536!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccac630121623%3A0x53386f2ac88991a9!2sTeatro%20Col%C3%B3n!5e0!3m2!1ses-419!2sar!4v1732310840488!5m2!1ses-419!2sar", 0, 2500,'https://www.arte-online.net/var/arte_online_net/storage/images/arte-online/agenda/exposiciones_muestras/piazzolla-100/893574-1-esl-AR/Piazzolla-100_nota.png'),
('FIESTA BRESH', 'fiestas', 'La fiesta de la juventud de Buenos Aires. La Bresh es una de las fiestas más populares entre los jóvenes, con una mezcla de reggaeton, trap, y música urbana, ¡y es un evento que no te podés perder!', 6000, 2500, '9 de Diciembre, 00:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.6459937458344!2d-58.37534491189754!3d-34.613112203207116!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95a3352ab8cb957f%3A0xa593c52c61dd7353!2sLa%20Trastienda!5e0!3m2!1ses-419!2sar!4v1732310905197!5m2!1ses-419!2sar", 1, 4000, 'https://ganaconacqua.com.ar/wp-content/uploads/2024/01/bresh-en-mar-del-plata.jpg'),
('Fiesta Flow', 'fiestas', 'La fiesta donde el reggaeton, trap y música urbana invaden la pista de baile. Ven a disfrutar de una noche inolvidable con los mejores DJs del género. ¡No te la podés perder!', 5000, 2000, '6 de Diciembre, 00:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d821.0708202233868!2d-58.44961449611492!3d-34.596997574950244!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb5f7e7b1bf9d%3A0xc41be2c95786e210!2sHumboldt%20189%2C%20C1414%20Villa%20Crespo%2C%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732310997615!5m2!1ses-419!2sar", 0, 2000, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiVhJ_Rt8CSVGtKvTJdiu_ug0u9fYcSBohZQ&s'),
('La Fiesta de la Cumbia y el Reggaeton', 'fiestas', 'Para los fanáticos de la cumbia, reggaeton y música latina, esta fiesta es el lugar perfecto para bailar hasta el amanecer. Ven a disfrutar de la mejor cumbia y reggaeton en un ambiente único.', 3500, 1500, '3 de Diciembre, 00:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.608305683734!2d-58.43278382365798!3d-34.5887763729597!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb588f4af5d17%3A0x560fe6ff3f099abf!2sPlaza%20Serrano!5e0!3m2!1ses-419!2sar!4v1732311098503!5m2!1ses-419!2sar", 0, 3000, 'https://i.ytimg.com/vi/UNIC7z882bY/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLA8wDaVPokoCoDZEcbzvFR7sbUd5Q'),
('El Circo de los Horrores', 'teatro', 'El Circo de los Horrores es un show único donde se mezcla el teatro con el circo y el horror. Espectáculos impactantes que desafían los límites de la mente humana, un verdadero despliegue de emoción y adrenalina.', 3000, 1000, '10 de Diciembre, 21:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.816460569773!2d-58.39012062365737!3d-34.60880237295253!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccac4b69ad5cf%3A0x9c60dd9663f59a45!2sLiceo!5e0!3m2!1ses-419!2sar!4v1732311143488!5m2!1ses-419!2sar", 1, 1500, 'https://teatromadrid.com/wp-content/uploads/2023/07/TEATRO_MADRID-Requiem-1-1100x733.jpg'),
('La Casa de Bernarda Alba', 'teatro', 'La obra de Federico García Lorca, "La Casa de Bernarda Alba", es un drama que explora la represión y el autoritarismo en una familia de mujeres. Un clásico del teatro español, de gran intensidad emocional.', 2000, 800, '14 de Diciembre, 20:30 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.9945242653957!2d-58.391015923657356!3d-34.60429997295416!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccac6a922a527%3A0x2f71173a6587ce2!2sTeatro%20San%20Mart%C3%ADn!5e0!3m2!1ses-419!2sar!4v1732312560783!5m2!1ses-419!2sar", 0, 1200, 'https://livepkassets.pechakucha.com/slides/e2bf7542-f138-4bee-83f1-f7f8976ed7c0/padblack_noborder_1600x900/slide_20_1614114932065.jpg'),
('Medea', 'teatro', 'Medea es una tragedia griega que explora temas como la venganza, la justicia y el amor. Esta versión contemporánea de la obra de Eurípides promete una puesta en escena desgarradora y llena de emoción.', 1500, 500, '16 de Diciembre, 20:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.122791594316!2d-58.38510562365756!3d-34.60105637295518!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccbfff9cecf1d%3A0x6ce16b300e73d19b!2sCerrito%20628%2C%20C1010AAN%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732312610299!5m2!1ses-419!2sar", 0, 1800, 'https://i0.wp.com/academiadesanromualdo.com/wp-content/uploads/2023/03/medea09.jpg?fit=1280%2C720&ssl=1'),
('Un Dios Salvaje', 'teatro', 'Una comedia negra que explora los límites del civismo y la moralidad en una reunión entre dos parejas que se enfrentan a la violencia latente detrás de las apariencias. Un teatro de gran tensión y humor ácido.', 2500, 1000, '18 de Diciembre, 21:30 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.0452139749764!2d-58.380526923657534!3d-34.603018172954556!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccace9a1ca877%3A0x9e9b4b95c7773b9c!2sTeatro%20Maipo!5e0!3m2!1ses-419!2sar!4v1732312646927!5m2!1ses-419!2sar", 0, 1000, 'https://img.alternativateatral.com/scripts/es/fotos/obras/resumen/000038716.jpg'),
('Festival de Cine Japonés', 'cultura japonesa', 'El Festival de Cine Japonés es el evento ideal para los amantes del cine asiático. Disfruta de una selección de las mejores películas japonesas actuales y clásicas, que exploran la riqueza cultural y el cine de Japón.', 2000, 800, '4 de Diciembre, 19:00 hs',"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.8179279063443!2d-58.39220752365724!3d-34.608765272952496!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccac34f79ce85%3A0x4a1be2e8ccfee711!2sCine%20Gaumont!5e0!3m2!1ses-419!2sar!4v1732312687748!5m2!1ses-419!2sar" , 1, 600, 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/XRCVQTNU5RDH3O2EOENYKFG25I.jpg'),
('Exposición de Arte Japonés', 'cultura japonesa', 'Una exposición única de arte japonés donde podrás disfrutar de las obras de artistas contemporáneos japoneses, así como una sección dedicada a la tradición artística ancestral del país. Una oportunidad para explorar el arte de Japón.', 1500, 600, '8 de Diciembre, 18:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.797528326207!2d-58.39557932365816!3d-34.58398937296122!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccaa199c2f643%3A0x49e543b8331abe7d!2sMuseo%20Nacional%20de%20Bellas%20Artes!5e0!3m2!1ses-419!2sar!4v1732312739310!5m2!1ses-419!2sar", 0, 500, 'https://images.pagina12.com.ar/styles/focal_16_9_960x540/public/2023-01/691265-museo-20nacional-20de-20arte-20oriental-0.jpg?h=29234840&itok=pHSnSRnv'),
('Festival del Hanami', 'cultura japonesa', 'Celebra el Hanami, la tradicional fiesta japonesa de observación de los cerezos en flor. En este festival podrás disfrutar de actividades culturales, danzas, música y una exhibición de sakura, el símbolo nacional de Japón.', 3000, 1200, '7 de Diciembre, 12:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3285.31560112615!2d-58.419677823658766!3d-34.57088007296604!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb59f0e33d4eb%3A0xb4d7c2d0044d32e!2sParque%20Tres%20de%20Febrero!5e0!3m2!1ses-419!2sar!4v1732312777442!5m2!1ses-419!2sar", 0, 200, 'https://www.clarin.com/2016/03/18/BJeXzToYEx_720x0.jpg'),
('Taller de Origami y Caligrafía Japonesa', 'cultura japonesa', 'Un taller interactivo donde podrás aprender el arte del origami (plegado de papel) y la caligrafía japonesa. Un evento para todos los interesados en la cultura japonesa y sus tradiciones más artísticas.', 500, 200, '10 de Diciembre, 15:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3285.31560112615!2d-58.419677823658766!3d-34.57088007296604!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb59f0e33d4eb%3A0xb4d7c2d0044d32e!2sParque%20Tres%20de%20Febrero!5e0!3m2!1ses-419!2sar!4v1732312777442!5m2!1ses-419!2sar", 0, 500, 'https://nichiagakuin.edu.ar/ngf/images/t_2016/clip_image008.jpg'),
('Liga Latinoamérica de League of Legends', 'esports', 'La Liga Latinoamérica (LLA) es la principal competencia de League of Legends en América Latina. Los mejores equipos de la región se enfrentan en un torneo de alta competencia y emoción. Un evento imperdible para los fanáticos del LoL.', 5000, 2000, '15 de Diciembre, 18:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.183821255318!2d-58.38699602365768!3d-34.59951297295591!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccac7ea9eea65%3A0xb3b57d11d4983037!2sAv.%20C%C3%B3rdoba%201234%2C%20C1055AAP%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732312883997!5m2!1ses-419!2sar", 1, 1000, 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/IVZZCTSBSRAYPDZVEJXP2SHBTA.jpg'),
('Torneo de Valorant: Copa Argentina', 'esports', 'Un torneo competitivo de Valorant en el que los mejores jugadores y equipos de Argentina luchan por el campeonato nacional. ¡Ven a ser parte de la emoción mientras los equipos de e-sports compiten por la gloria!', 3000, 1200, '20 de Diciembre, 17:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.808971074338!2d-58.39242502365827!3d-34.58369987296143!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccaa12e375b6d%3A0x3f9f935dc99bf4fb!2sCentro%20de%20Convenciones%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732312922697!5m2!1ses-419!2sar", 0, 800, 'https://www.telefonica.com.ar/wp-content/uploads/sites/12/2023/07/Copa-Movistar-Fibra.jpg?w=1224&h=673&crop=1'),
('FIFA 24: Torneo Internacional', 'esports', 'Participa en uno de los torneos de FIFA más prestigiosos, donde jugadores de todo el mundo se enfrentan en intensas rondas para conseguir el título. ¡Demuestra que eres el mejor en el simulador de fútbol más famoso del mundo!', 1500, 600, '22 de Diciembre, 19:30 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.78643721655!2d-58.38888382365728!3d-34.60956147295226!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccadb2f4dc7b9%3A0x42248263d88e9561!2sAv.%20de%20Mayo%201400%2C%20C1076%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732312971393!5m2!1ses-419!2sar", 0, 700, 'https://phantom-marca.unidadeditorial.es/16534a711499d3f65810a95abb971c77/resize/828/f/jpg/assets/multimedia/imagenes/2024/02/05/17071550474357.jpg'),
('The International Dota 2: Fase de Clasificación', 'esports', 'Un evento clave para los fanáticos de Dota 2, donde los equipos se enfrentan en la fase clasificatoria de The International, el torneo de e-sports más grande de Dota 2. ¡Ven a ver la acción en vivo y a apoyar a tu equipo favorito!', 4000, 1500, '25 de Diciembre, 14:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.6939231721717!2d-58.41654452365791!3d-34.586610472960466!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb57e2e8a59e7%3A0x164ba7a68edfa1cc!2sAv.%20Sta.%20Fe%203500%2C%20C1425%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732313016393!5m2!1ses-419!2sar", 0, 1000, 'https://larepublica.cronosmedia.glr.pe/original/2021/10/09/6162181c82f48a096e35f1a4.jpg'),
('Carlos Latre: Show en Vivo', 'Stand up', 'Carlos Latre, uno de los comediantes más conocidos de Argentina, se presenta en vivo con un show lleno de humor y personajes. Una noche de risas garantizadas con el estilo único de Latre.', 1000, 500, '5 de Diciembre, 21:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.030617816592!2d-58.38144152365744!3d-34.60338727295435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccaceed5746b9%3A0xf933ab84305babc0!2sTeatro%20Gran%20Rex!5e0!3m2!1ses-419!2sar!4v1732313086947!5m2!1ses-419!2sar", 0, 1500, 'https://cineytele.com/play/wp-content/uploads/2023/04/carlos-latre-oneman-show-cartel.jpg'),
('La Noche de la Comedia', 'Stand up', 'El ciclo de comedia más divertido de Buenos Aires, con diferentes comediantes de la escena local presentando sus mejores monólogos en un show variado y lleno de humor.', 600, 300, '7 de Diciembre, 22:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.030617816592!2d-58.38144152365744!3d-34.60338727295435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95a3352abefff29f%3A0x192c01e9afb3457b!2sBalcarce%20460%2C%20C1064AAJ%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732313118496!5m2!1ses-419!2sar", 0, 500, 'https://imgplateanet.com.ar/imagenes/img/imagenes/425x318/noches-de-comedia-stand-up.jpg'),
('Martín Garabal: Stand-Up Comedy', 'Stand up', 'Martín Garabal, uno de los comediantes más destacados de la escena argentina, regresa con un show de stand-up donde se burla de la vida cotidiana, las redes sociales y más.', 800, 400, '10 de Diciembre, 20:30 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.995343649225!2d-58.429674723658465!3d-34.57898437296329!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb59a95e91497%3A0x1bda92d7310f9cc8!2sAv.%20Juan%20Bautista%20Justo%20620%2C%20C1425%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732313153129!5m2!1ses-419!2sar", 1, 800, 'https://cloudfront-us-east-1.images.arcpublishing.com/grupoclarin/6Q6PUQ4RLFGZHIXNU742GE22JQ.jpeg'),
('Las Pelotas del Stand-Up', 'Stand up', 'Un espectáculo de comedia en donde varios comediantes presentan su mejor material, en una noche llena de risas y diversión. ¡Ideal para pasar una noche divertida con amigos!', 400, 150, '12 de Diciembre, 23:00 hs', "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.3380641369167!2d-58.43214951190192!3d-34.59561200322936!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcca79f5b42d0f%3A0x7f38f34eeb025b33!2sAv.%20C%C3%B3rdoba%204335%2C%20C1414%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses-419!2sar!4v1732313287355!5m2!1ses-419!2sar", 0, 600, 'https://standupclubarg.com/wp-content/uploads/2023/09/e7b40f87-155d-4016-b01f-375ba5984fc5-edited.webp');


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
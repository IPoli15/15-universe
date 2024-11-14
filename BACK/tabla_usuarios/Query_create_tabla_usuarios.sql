USE universe;

CREATE TABLE IF NOT EXISTS `usuarios` (
  id  INT AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(50),
  password varchar(50)
);

INSERT INTO usuarios (nombre, password)

VALUES
('alejandro' , '111'),
('henry' , '441'),
('blas' , '123'),
('yohara' , '555'),
('nacho' , '789'),
('santiago' , '631'),
('ruy' , '911');

SELECT *
FROM `usuarios`
LIMIT 1000;

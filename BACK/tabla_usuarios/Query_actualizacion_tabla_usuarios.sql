USE universe;

ALTER TABLE usuarios
DROP PRIMARY KEY,
CHANGE id id_usuarios INT AUTO_INCREMENT PRIMARY KEY;

SELECT *
FROM `usuarios`
LIMIT 1000;
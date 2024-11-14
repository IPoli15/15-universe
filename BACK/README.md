Esta prueba de creacion de base de datos esta conecta con la mia no se como subirlo, tarea a realizar con ayuda de los compañeros. 
en caso de que alguno quiera probar conectandolo con el suyo, esto es lo q hice
en mi caso uso mysql workbench
pip install mysql-connector
pip install --upgrade mysql-connector-python

db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': '*****', *aqui debe ir la contraseña que le hayan puesto a su base*
    'database': 'eventos' *este es el nombre de la base de datos q yo cree, en casa de que tengan otra coloquen esa*
}

en mi caso tuve q cambiar mi plugin de actualizacion porque me genero problemas hice lo siguiente en la terminal
mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'su contraseña';
FLUSH PRIVILEGES;
EXIT;
por las dudas reinicien la base su base de datos con esto
sudo systemctl restart mysql

y nada cualquier cosa me preguntan 

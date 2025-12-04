#Flask Migrate

#Instalacion

pip install flasl-migrate

##Uso

# Crea la conifguracion de la base de datos
#se ejecuta una sola vez
flask db init

#Genera los scripts de migraciones
flask db migrate -m "Create user table"

#Aplicar las migraciones generadas
flask bd upgrade
# PC2 API

El código del backend de encuentra dentro de la carpeta **app**

Requisitos tecnicos para poder correr el backend
- Tener docker instalado en la maquina donde se va a ejecutar el proyecto
- Configurar las variables de entorno
- Ejecutar los comandos de migracion y creacion de super usuario en orden

### Configurar el entorno por primera vez
en la raiz del proyecto existe un archivo llamado** env.template**
este archivo contiene nuestras variables de entorno con valores por defectos
usted puede cambiarlos por los valores que quiera

**nota: no recomiendo cambiar el host de postgres si vamos a ejecutar nuestro ambiente de manera local**

Para que el backend pueda funcionar debe usted hacer una copia del archivo con el siguiente comando:

`cp env.template .env`

Una vez copiado se puede iniciar con la construccion de la imagen de docker y posteriormente la puesta en marcha de esta misma, para hacerlo puede utilizar el siguiente comando:

`docker-compose up -d --build`


Si todo sale done podremos ir al [http://0.0.0.0:3002/](http://0.0.0.0:3002/ "http://0.0.0.0:3002/") donde vive nuestra app y podremos ver la documentación de la api.

Lo siguiente que debemos hacer es seguir estos comandos para aplicar las migraciones y crear un usuario en nuestro administrador:
- `docker-compose exec app python3 manage.py makemigrations`
- `docker-compose exec app python3 manage.py migrate`
Nota: También podemos ejecutar el script ./migrate_db.sh

Para crear un super usuario en nuestro administrador debemos ejecutar el siguiente comando:

`docker-compose exec app python3 manage.py createsuperuser`
Nota: También podemos ejecutar el script ./createuser.sh

Para poder hacer uso de nuestro backend debemos crear las tiendas en el admin y usuarios de las tiendas, luego debemos logearnos en nuestra aplicación de angular y podemos ver funcionando la aplicación conectada al backend.

Si queremos detener nuestra imagen podemos hacerlo con este comando:

`docker-compose stop`

Si queremos volver a levantar nuestra nuevamente:
`docker-compose up -d`

Nota: También podemos ejecutar el script ./rebuild_container.sh para hacer ambas cosas en un sólo comando

###Para el archivo CSV, por defecto hemos definido el orden como:
Nombre de usuario | Contraseña | Id de evento |
El archivo puede o no tener encabezado, debemos indicarlo en el formulario de carga del archivo

##Visual
El host en el que cargamos la interfaz se encuenta en:
http://0.0.0.0:3002/views/authenticator# pc2usersadmin

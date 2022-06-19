# Portal Millonario

El código del backend se encuentra dentro de la carpeta **app**

Requisitos técnicos para poder correr el backend
- Tener docker instalado en la máquina donde se va a ejecutar el proyecto
- Configurar las variables de entorno
- Ejecutar los comandos de migración y creación de superusuario en orden

### Configurar el entorno por primera vez
En la raíz del proyecto existe un archivo llamado** env.template**
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

Para crear un superusuario en nuestro administrador debemos ejecutar el siguiente comando:

`docker-compose exec app python3 manage.py createsuperuser`
Nota: También podemos ejecutar el script ./createuser.sh

Para poder hacer uso de nuestro backend debemos crear las tiendas en el admin y usuarios de las tiendas, luego debemos loguearnos en nuestra aplicación de angular y podemos ver funcionando la aplicación conectada al backend.

Si queremos detener nuestra imagen podemos hacerlo con este comando:

`docker-compose stop`

Si queremos volver a levantar nuestra nuevamente:
`docker-compose up -d`

Nota: También podemos ejecutar el script ./rebuild_container.sh para hacer ambas cosas en un sólo comando

###Play with Docker
Para correr el backend desde un remoto y sin necesidad de instalar nada en nuestro equipo debemos ir a
[Play with Docker](https://labs.play-with-docker.com/), en caso de no tener una cuenta de Docker la debemos crear.
Posterior a ello creamos una instancia en el botón *Add new instance* y en ella ejecutaremos todo lo que procede:

```
git clone https://github.com/JoelBorrero/portal_millonario_backend.git
cd portal_millonario_backend
cp env.template .env
./rebuild-container.sh
./migrate_db.sh
docker-compose exec app python3 manage.py shell
>>> from backend.apps.utils.demo_info import *
>>> perform_create()
```

Una vez hecho esto, en caso de no tener el puerto `3002` expuesto, debemos hacerlo para acceder a nuestro backend de una forma remota.

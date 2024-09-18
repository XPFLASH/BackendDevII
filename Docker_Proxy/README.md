# Docker Proxy

## Requisitos Previos

Es necesario tener instalado [**Docker**](https://docs.docker.com/)

## Instrucciones

Configurar un Docker con Nginx con el puerto 80 para posteriormente instalar dentro de ese Docker Python , crear un usuario y ejecutar el ejemplo de FLASK, configurar proxy para responder por enpoint /pagina para resolver el puerto 5000 del FLASK.

## Proceso

Desde la terminal (en algún lugar o carpeta de nuestro gusto) debemos ejecutar el siguiente comando:

```bash
docker pull nginx
```
![docker nginx pull](./images/nginx_pull.png)

En donde con esto nos instalara la version más reciente de nginx, igualmente si queremos alguna versión valida en especifico debemos poner seguido de nginx ":version", como se muestra a continuación, aunque es recomendable tener la versión más actual

```bash
docker pull nginx:1.13.7
```
Posteriormente para poder ver la imagen descargada debemos ejecutar el comando:

```bash
docker images
```
![docker images](./images/docker_images.png)

Para crear un Docker, tendremos que ejecutar el siguiente comando:

```bash
docker run --name nombreContenedor -d -p 80:80 nginx
```
![docker run](./images/docker_run.png)

En donde se mapea el puerto 80 del Contenedor con el puerto 80 de la maquina, creando así el contenedor de imagen Nginx ('-d' indica que se esta ejecutando el contenedor en 2do plano)

Una vez ya creado el contenedor, podemos verificar su creación ejecutando el comando, que se utiliza para poder listar los contenedores en Docker

```bash
docker ps
```
![docker run](./images/docker_ps.png)

Para poder detener el contenedor se necesita ejecutar el comando:

```bash
docker stop nombreContenedor
```
Despues de detener el contendor, nos vamos a dirigir a la ruta en donde se esta almacenando nuestro Docker por lo que vamos a un editor de codigo para añadirle unos archivos

#### 1. docker-compose.yml
#### 2. Dokerfile
#### 3. nginx.conf
#### 4. main.py

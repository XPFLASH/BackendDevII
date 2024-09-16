Configurar un Docker con Nginx con el puerto 80
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
En donde con esto nos instalara la version más reciente de nginx, igualmente si queremos alguna versión valida en especifico debemos poner seguido de nginx ":version", como se muestra a continuación, aunque es recomendable tener la versión más actual

```bash
docker pull nginx:1.13.7
```
Posteriormente para poder ver la imagen descargada debemos ejecutar el comando:

```bash
docker images
```
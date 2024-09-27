# Docker PostgreSQL

#### Alumno: Escobar Ceseña Ricardo
#### Grupo: 9SE

## Requisitos Previos

Es necesario tener instalado [**Docker**](https://docs.docker.com/)

## Instrucciones

- Crear Docker, exponer su puerto y crear la base de datos que se anexa en el apartado de Attach, ejecutar el script para generar informacion FAKE. 
- Anexar pantallas para comprobar lo antes solicitado.

## Proceso

Desde la terminal (en algún lugar o carpeta de nuestro gusto) debemos ejecutar el siguiente comando:

```bash
docker pull postgres:13
```
![docker postgree pull](./images/postgree_pull.png)

En donde con esto nos instalara una version de postgres, igualmente si queremos alguna versión valida en especifico debemos poner seguido de postgres ":version" o bien tener la versión mas actualizada debemos poner postgres ":latest"

```bash
docker pull postgres:latest
```
Una vez ya descargada la imagen para poder confirmarla debemos ejecutar el comando:

```bash
docker images
```
![docker images](./images/docker_images.png)

Para crear un Docker, tendremos que ejecutar el siguiente comando:

```bash
docker run --name nombreContenedor -e POSTGRES_PASSWORD=tuContraseña -d -p 80:80 postgres:13
```
![docker run](./images/docker_run.png)

Aqui definos una contraseña así como se mapea el puerto 80 del Contenedor con el puerto 80 de la maquina, creando así el contenedor con la imagen de Postgres ( '-e' significa que se permite establecer variables de entorno dentro del contenedor mientras '-d' indica que se esta ejecutando el contenedor en 2do plano)

**NOTA**:  PostgreSQL usa el puerto 5432, para acceder a PostgreSQL desde fuera del contenedor hay que mapear el puerto 5432
```bash
-p 5432:5432
```

Una vez ya creado el contenedor, podemos verificar su creación ejecutando el comando que se utiliza para poder listar los contenedores en Docker

```bash
docker ps
```
![docker ps](./images/docker_ps.png)

Para poder detener el contenedor se necesita ejecutar el comando:

Ahora nos vamos a dirigir a la ruta en donde se esta almacenando nuestro Docker por lo que vamos a un editor de codigo para añadirle los siguientes archivos:

#### 1. docker-compose.yml
Es un archivo de configuración que se usa para poder definir y ejecutar múltiples servicios Docker dentro de un solo entorno. (Se pueden definir varios atributos como el nombre, version, puertos, etc).

![docker compose_yml](./images/docker_compose_yml.png)

#### 2. Querys
Son archivos de texto que contienen una o más instrucciones o consultas SQL (Structured Query Language), estas consultas se utilizan para interactuar con bases de datos, permitiendo realizar tareas como seleccionar, insertar, actualizar o eliminar datos en una base de datos.

![querys_sql](./images/querys_sql.png)

Al ya tener los archivos ejecutamos el comando docker-compose up para poder levantar el servicio postgreSQL en el archivo docker-compose.yml

```bash
docker-compose up
```
![docker_compose](./images/docker_compose_up.png)

Podemos verificar en el Docker Desktop que se estan compilando y ejecutando el servicios dentro del contenedor

![docker_container](./images/docker_postsql.png)

Ahora necesitamos copiar los archivos locales desde la maquina local hasta el interior del contenedor en Docker, esto lo hacemos para poder ejecutar los querys de modo que podamos acceder a la base de datos, para ello debemos ejecutar el siguiente comando:

```bash
docker cp <ruta_local>/<nombre_archivo> <nombre_contenedor>-<ruta_destino_contenedor>:/<nombre_archivo>
```
![copy_querys](./images/docker_copy_querys.png)

Una vez ya copiados y puestos dentro de nuestro contenedor, lo siguiente que se tienen que hacer es ejecutarlos para que configuren la base de datos para ello debemos ejecutar lo siguiente para cada uno de los archivos:

```bash
docker exec -it <nombre_contenedor> psql -U <usuario> -d <base_de_datos> -f <ruta_archivo_sql>
```
**NOTA**: ***psql*** es el cliente de línea de comandos de PostgreSQL.

![exec_query_base](./images/exec_query_base.png)
![exec_query](./images/exec_query.png)

Una vez ya ejecutados los archivos querys, ahora debemos ejecutar nuestro contenedor por lo que debemos ejecutar el siguiente comando:

```bash
docker exec -it <nombre_contenedor> psql -U <usuario> -d <base_de_datos>
```
En caso de que salga bien, ahora podremos ingresar a la base de datos, en donde para poder consulta las tablas que estan dentro de la base de datos debemos poner **\dt**

![ejecutar_db](./images/exec_dataBase.png)

Ya dentro de la base de datos podemos realizar operaciones como **SELECT** o **INSERT** por lo que ahora vamos a realizar algunas operaciones

![capturar_datos](./images/captura_datos.png)
![capturar_datos2](./images/captura_datos2.png)

Ya para finalizar, si queremos salir debemos ejecutar **\q**, con esto saldremos de la base de datos

![salir](./images/salir.png)

Cerramos nuestro contenedor, ya sea desde Docker Desktop o desde la terminal ejecutando el comando:

```bash
docker stop nombreContenedor
```

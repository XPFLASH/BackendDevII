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
![docker ps](./images/docker_ps.png)
![docker compose_yml](./images/docker_compose_yml.png)
![querys_sql](./images/querys_sql.png)
![docker_compose](./images/docker_compose_up.png)
![docker_container](./images/docker_postsql.png)
![copy_querys](./images/docker_copy_querys.png)
![exec_query_base](./images/exec_query_base.png)
![exec_query](./images/exec_query.png)
![ejecutar_db](./images/exec_dataBase.png)
![capturar_datos](./images/captura_datos.png)
![capturar_datos2](./images/captura_datos2.png)
![salir](./images/salir.png)

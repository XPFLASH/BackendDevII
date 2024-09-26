# ChatCMD

## Instrucciones

Utilizando el codigo del socket server-client para que acepte comandos por parte del cliente.

Ejemplo:

cliente> lsFiles    (Nos regresara el listado de los archivos que se encuentran en el folder de "Files" en la misma ruta donde se esta ejecutando el server.)

- **movies.json**
- **archivo.txt**

cliente>get archivo.txt  (El servidor debera enviar el achivo al cliente, el cliente debera crear un folder "download" y guardar el archivo ahi mismo.)

***Recordar que al enviar un comando no debera replicarse a los demas clientes conectados***

## ¿Como usarlo?

Para poder usar este chat, es necesario tener abierta 3 terminales con la ruta de la carpeta en donde tenemos este proyecto (Ya sea en Visual Studio o CMD):

- 1 terminal ejecutando el archivo **server-socket.py**
```bash
python server-socket.py 
```
- 2 terminales ejecutando el archivo **cliente-socket.py**
 ```bash
python server-socket.py 
```

Al momento de ejecutar el servidor este nos permitira comunicarnos entre las 2 terminales del cliente, ya en estas podemos comenzar a chatear en donde en cualquiera de las 2 podemos recibir como enviar mensajes.

En caso de querer salir de la ejeccución en la parte del cliente debemos escribir solamente **salir** igualmente aplica para detener la ejecucción del servidor.

## Comandos

Para este proyecto existen 2 comandos

El primero es **IsFiles**, con este nosotros se nos muestra el contenido de la carpeta *files*, donde se nos genera una especie de lista con todos los archivos que las conforma, para poder ejecutar simplemente se debe escribir:
 ```bash
IsFiles 
```
(Es importante escribirlo tal como esta, porque de lo contrario no se va a ejecutar)

El segundo es **get nombreArchivo.txt**, con este nosotros podemos guardar cualquier archivo que este donde en la carpeta de *files* dentro de la carpeta de *downland*, en donde en caso de no tenerla se nos va generar una para poderlo almacenarlo, aqui debemos escribir **get** junto con el nombre y terminacion del archivo, debemos procurar escribir bien el nombre de lo contrario no se va guardar
 ```bash
get archivo.txt
```
(Es importante cuidar los espacios y checar que exitan los archivos por lo que es recomendable ejecutar primero el comando anterior para mostrarnos los archivos que existen)

**NOTA**: estos comandos al momento de ejecutarse una terminal cliente no se veran reflejados en la otra terminal cliente



# pylint:disable=all

import socket
import threading
import sys
import pickle
import os

class Servidor():
    def __init__(self, host="localhost", port=7000):
        # Arreglo para guardar los clientes conectados
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        # Hilos para aceptar y procesar las conexiones
        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)

        aceptar.daemon = True 
        aceptar.start()
        procesar.daemon = True 
        procesar.start()

        try:
            while True:
                msg = input('-> ')
                if msg == 'salir':
                    break
            self.sock.close()
            sys.exit()
        except:
            self.sock.close()
            sys.exit()

    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msg)
            except:
                self.clientes.remove(c)
        
    def aceptarCon(self):
        print("aceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
            except:
                pass
    
    
    def listar_archivos(self, cliente):
        path = './files' 
        with os.scandir(path) as entries: 
                archivos = [entry.name for entry in entries if entry.is_file() or entry.is_dir()]
                if archivos:
                    respuesta = "Archivos:\n" + "\n".join(archivos)
                else:
                    respuesta = "No hay archivos en la carpeta."

        cliente.send(pickle.dumps(respuesta))
    
    def enviar_archivo(self, archivo, cliente):
        path = './files/' + archivo
        with open(path, 'rb') as f:
            data = f.read()
            cliente.send(pickle.dumps((archivo, data)))
    

    def procesarCon(self):
        print("ProcesarCon iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            msg = pickle.loads(data)
                            if msg == 'IsFiles':
                                self.listar_archivos(c)
                                
                            elif msg.startswith('get '):
                                archivo = msg.split(' ')[1] 
                                self.enviar_archivo(archivo, c)
                                
                            else:
                                self.msg_to_all(data, c)
                    except:
                        pass

if __name__ == "__main__":
    servidor = Servidor()

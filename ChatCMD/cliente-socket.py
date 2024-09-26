# pylint:disable=all

import socket
import threading
import sys
import pickle
import os

class Cliente():
    def __init__(self, host="localhost", port=7000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))
        msg_recv = threading.Thread(target=self.msg_recv)
        msg_recv.daemon = True 
        msg_recv.start()

        while True:
            msg = input('-> ')
            if msg.startswith('get '):
                self.send_msg(msg)

            elif msg != 'salir':
                self.send_msg(msg)
            
            elif msg == 'IsFiles': 
                self.send_msg(msg)
        
            else:
                self.sock.close()
                sys.exit()
     
    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1028)
                if data:
                    data = pickle.loads(data)
                    if isinstance(data, tuple) and isinstance(data[1], bytes):
                        self.guardar_archivo(data[0], data[1])
                    else:
                        print(data)
            except:
                pass
    

    def send_msg(self, msg):
        try:
            self.sock.send(pickle.dumps(msg))
        except:
            print('error')
    
    
    def guardar_archivo(self, nombre_archivo, data):
        if not os.path.exists('download'):
            os.makedirs('download')

        path = './download/' + nombre_archivo
        with open(path, 'wb') as f:
            f.write(data)
        print(f"Archivo '{nombre_archivo}' guardado en {path}")

if __name__ == "__main__":
    cliente = Cliente()
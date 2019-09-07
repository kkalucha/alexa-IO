import time
import socket

class InterfaceLib:
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 65432

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

    def INPUT(self):
        data = self.sock.recv(1024)
        return data.decode()
    
    def PRINT(self, output):
        self.sock.sendall(output.encode())

    def idunno(self):
        PRINT("I don't know that. Answer again in the next 5 seconds...")
        time.sleep(5)

    def noans(self):
        PRINT("You didn't answer. Answer again in the next 5 seconds...")
        time.sleep(5)
        
    def __del__(self):
        self.sock.close()
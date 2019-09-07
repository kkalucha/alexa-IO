import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def INPUT():
    data = s.recv(1024)
    return data.decode()
    
def PRINT(output):
    s.sendall(output.encode())
    
PRINT('she said do you love me?')

if (INPUT() == 'yes'):
    PRINT('you said yes')
else:
    PRINT('you said no')
    
s.close()
import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print('connected by', addr)

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def interact():
    data = conn.recv(1024)
    if not data:
        return statement('bye')
    return question(data.decode())

@ask.intent("AMAZON.YesIntent")
def yes_intent():
    conn.sendall('yes'.encode())
    return interact()
    
@ask.intent("AMAZON.NoIntent")
def no_intent():
    conn.sendall('no'.encode())
    return interact()

@ask.intent("FoodIntent", mapping = {'Food' : 'Food'})
def food_intent(Food):
    conn.sendall(Food.encode())
    return interact()
    
if __name__ == '__main__':
    app.run(port = 12345)

conn.close()
s.close()
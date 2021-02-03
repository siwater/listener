import logging
import threading

from flask import Flask, render_template
from time import sleep

def listen():
    i = 0
    while True:
         i += 1
         print(f'Listening {i}')
         sleep(5)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", title="Greetings", target="world")

if __name__ == "__main__":
    listener = threading.Thread(target=listen)
    listener.start() 
    app.run(host='0.0.0.0', port=8081)

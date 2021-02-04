#
# Simulation of an event listen loop in a process that also exposes 
# an HTTP endpoint (e.g. for command & control) 
#
import os
import sys
import threading

from flask import Flask, render_template, jsonify
from time import sleep

def listen():
    i = 0
    while True:
         i += 1
         print(f'Listener iteration #{i}')
         sleep(5)

listen_port = os.environ.get('BACKEND_PORT')
if listen_port == None:
    sys.exit('LISTEN_PORT undefined')


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", title="Greetings", target="from the listener")

@app.route('/message', methods=['GET'])
def message():
    return jsonify({"message": "Listener awaiting your command"})

if __name__ == "__main__":
    listener = threading.Thread(target=listen)
    listener.start() 
    app.run(host='0.0.0.0', port=listen_port)

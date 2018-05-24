import eventlet

eventlet.monkey_patch()
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import webbrowser
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    if str(message)=='connected':
        for i in range(5,10):
            print(i)
            socketio.emit('count', {'data': i})
            time.sleep(1)

if __name__ == '__main__':
    webbrowser.open(url='http://127.0.0.1:5000/')
    socketio.run(app)

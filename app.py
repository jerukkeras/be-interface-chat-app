from flask import Flask
from flask_socketio import SocketIO, join_room

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@socketio.on('connect')
def test_connect():
    print('Client connected')
    socketio.emit('my response', {'data': 'Connected'})

@socketio.on('join_room')
def handle_join_room(data):
    room_id = data['room']
    join_room(room_id)
    print(f'Client joined room: {room_id}')

@socketio.on('client_message')
def handle_client_message(data):
    room_id = data['room']
    message = data['message']
    print(f'Received message from client in room {room_id}: {message}')
    socketio.emit('message', data , room=room_id)

if __name__ == '__main__':
    socketio.run(app, debug=True)

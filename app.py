from flask import Flask
from flask_socketio import SocketIO, join_room

from chat.chat_routes import chat
from game.game_routes import game
from game_data.game_data_models import save_data
from game_master.game_master_routes import game_master

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


app.register_blueprint(game, url_prefix='/game')
app.register_blueprint(game_master, url_prefix='/game_master')
app.register_blueprint(chat, url_prefix='/chat')


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
    print(data, type(data))
    try:
        saved_data = save_data({
            'chat_from': data['username'],
            'chat_to': data['room'],
            'chat_text': data['message'],
            'room_id': data['roomId']
        })
        socketio.emit('message'+data["roomId"], saved_data)
    except Exception as e:
        socketio.emit("error", {
            "status": "error",
            "message": str(e),
        })


if __name__ == '__main__':
    socketio.run(app, debug=True)

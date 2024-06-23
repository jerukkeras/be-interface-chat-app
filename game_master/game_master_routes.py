from flask import Blueprint, jsonify, request
from game_master.game_master_models import add_room, get_rooms_by_admin


game_master = Blueprint('game_master', __name__)


@game_master.route('/<password>/generate/room', methods=['POST'])
def generate_room(password: str):
    if password != 'password123':
        return jsonify({'error': 'Invalid password'}), 401
    try:
        data = request.json
        room = {
            'name': data['name'],
            'description': data['description'],
            'room_password': data['room_password']
        }
        generated_room = add_room(room)
        return generated_room, 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@game_master.route('/<password>/game/<key>/room', methods=['GET'])
def admin_get_room_by_key(password: str, key: str):
    try:
        rooms = get_rooms_by_admin(key, password)
        return rooms
    except Exception as e:
        return {'error': str(e)}


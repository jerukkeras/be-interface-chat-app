from flask import jsonify, Blueprint
from game.game_models import get_rooms


game = Blueprint('game', __name__)


@game.route('/<key>/room', methods=['GET'])
def get_room_by_key(key: str):
    try:
        rooms = get_rooms(key)
        return jsonify(rooms), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

from config import supabase


def add_room(room: dict):
    generated_room = supabase.table('room').insert(room).execute()
    return generated_room


def get_rooms_by_admin(room_id: str, password: str):
    rooms = supabase.table('room').select('room_id, name, description, created_date, modified_by').eq('room_id', room_id).eq('room_password', password).execute()
    rooms = rooms.data
    return rooms

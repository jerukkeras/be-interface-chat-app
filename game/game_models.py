from config import supabase


def get_rooms(room_id: str):
    rooms = supabase.table('room').select('room_id, name, description, created_date, modified_by').eq('room_id', room_id).execute()
    rooms = rooms.data
    return rooms


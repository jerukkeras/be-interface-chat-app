from config import supabase


def get_all_data(room_id):
    data = supabase.table('room_data').select('*').eq('room_id', room_id).execute()
    data = data.data
    return data


def save_data(data):
    saved_data = supabase.table('chat').insert(data).execute()
    saved_data = saved_data.data
    return saved_data

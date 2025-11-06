from .database import conn
from util.get_time_now import get_time_now

def messages(user_id: str, message: str, name: str):
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO messages ( user_id, name, message, data ) VALUES (%s, %s, %s, %s);""", 
                (user_id, name, message, get_time_now()))
    conn.commit()

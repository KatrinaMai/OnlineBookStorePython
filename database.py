import sqlite3
import os

PATH = os.path.dirname(os.path.abspath(__file__))
BOOKSTORE_DB = os.path.join(PATH, "bookstore.db")

def get_db_connection():
    conn = sqlite3.connect(BOOKSTORE_DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    schema_path = os.path.join(PATH, "create_schema.sql")
    data_path = os.path.join(PATH, "initialize_data.sql")
    
    db_exists = os.path.exists(BOOKSTORE_DB)
    conn = get_db_connection()
    
    if not db_exists:
        try:
            # Read and execute schema.sql
            with open(schema_path, "r", encoding="utf-8") as f:
                conn.executescript(f.read())
            
            # Read and execute data.sql
            with open(data_path, "r", encoding="utf-8") as f:
                conn.executescript(f.read())
                
            conn.commit()
            print("Database successfully initialized from create_schema.sql and initialize_data.sql!")
        except Exception as e:
            print(f"Error executing SQL files: {e}")
            raise e
            
    conn.close()

def query_db(query, args=(), one=False):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        return (rv[0] if rv else None) if one else rv
    finally:
        conn.close()

def execute_db(query, args=()):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute(query, args)
        conn.commit()
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
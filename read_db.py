import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'evaluations.db')

def read_database_contents():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        print(f"\n--- Contenido de la tabla Tcriterios en {DB_FILE} ---")
        cursor.execute("SELECT * FROM Tcriterios")
        rows = cursor.fetchall()
        if rows:
            # Print headers
            headers = [description[0] for description in cursor.description]
            print(" | ".join(headers))
            print("-" * (sum(len(h) for h in headers) + 3 * (len(headers) - 1)))
            for row in rows:
                print(" | ".join(map(str, row)))
        else:
            print("La tabla Tcriterios está vacía.")

        print(f"\n--- Contenido de la tabla Tsumatorias en {DB_FILE} ---")
        cursor.execute("SELECT * FROM Tsumatorias")
        rows = cursor.fetchall()
        if rows:
            # Print headers
            headers = [description[0] for description in cursor.description]
            print(" | ".join(headers))
            print("-" * (sum(len(h) for h in headers) + 3 * (len(headers) - 1)))
            for row in rows:
                print(" | ".join(map(str, row)))
        else:
            print("La tabla Tsumatorias está vacía.")

    except sqlite3.Error as e:
        print(f"Error al conectar o leer la base de datos: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    read_database_contents()

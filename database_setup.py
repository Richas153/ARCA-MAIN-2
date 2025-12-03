import sqlite3
import os

DB_FILE = "arca_db.sqlite"
TABLE_NAME = "evaluations"

def setup_database():
    """Crea la base de datos y la tabla si no existen."""
    # No hacemos nada si el archivo ya existe para no borrar datos.
    if os.path.exists(DB_FILE):
        return

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Crear tabla con los 18 campos
        cursor.execute(f'''
        CREATE TABLE {TABLE_NAME} (
            NameInterview TEXT PRIMARY KEY,
            A1_Studies_Intentions REAL,
            A2_Hobbies REAL,
            A3_Foreigner_Local REAL,
            A4_Living_Environment REAL,
            A5_Work_Location REAL,
            B1_Salary_Expectation REAL,
            B2_Payment_Model REAL,
            C1_Profile_Fit REAL,
            C2_Workload_Test REAL,
            C3_Leadership REAL,
            D1_Language_Req REAL,
            D2_Schedule_Req REAL,
            D3_Location_Req REAL,
            D4_Profile_Req REAL,
            D5_Benefits_Comp REAL,
            Total REAL,
            Justificacion TEXT
        )
        ''')

        conn.commit()
        print(f"(+) Base de datos '{DB_FILE}' y tabla '{TABLE_NAME}' creadas exitosamente.")
    except sqlite3.Error as e:
        print(f"[Error] Ocurrió un error al configurar la base de datos: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()
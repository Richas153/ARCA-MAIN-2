import os
import glob
import sqlite3
import subprocess
import re

INPUT_DIR = "in"
OUTPUT_DIR = "out"
DB_FILE = "arca_db.sqlite"
DB_TABLE = "evaluations"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "consolidated_results.csv")
CSV_HEADER = "NameInterview,A1_Studies_Intentions,A2_Hobbies,A3_Foreigner_Local,A4_Living_Environment,A5_Work_Location,B1_Salary_Expectation,B2_Payment_Model,C1_Profile_Fit,C2_Workload_Test,C3_Leadership,D1_Language_Req,D2_Schedule_Req,D3_Location_Req,D4_Profile_Req,D5_Benefits_Comp,Total,Justificacion"

def gemini_analyze(vtt_filename):
    """
    Reads the analysis result from a corresponding .txt file in the output directory.
    """
    base_filename, _ = os.path.splitext(vtt_filename)
    analysis_filepath = os.path.join(OUTPUT_DIR, f"{base_filename}.txt")
    
    if os.path.exists(analysis_filepath):
        try:
            with open(analysis_filepath, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except Exception as e:
            print(f"    [Error] Could not read analysis file {analysis_filepath}: {e}")
            return None
    return None

def setup_database():
    print("Verificando la configuración de la base de datos...")
    try:
        # Use shell=True for Windows compatibility
        subprocess.run(["python", "database_setup.py"], check=True, capture_output=True, text=True, encoding='utf-8', shell=True)
        print("✔ Verificación de base de datos completada.")
    except subprocess.CalledProcessError as e:
        print(f"[Error] El script database_setup.py falló:")
        print(e.stderr)
        raise

def get_processed_names(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT NameInterview FROM {DB_TABLE}")
        return {row[0] for row in cursor.fetchall()}
    except sqlite3.Error:
        return set()

def validate_and_parse_csv_line(csv_line):
    fields = csv_line.split(',', 17)
    if len(fields) != 18:
        print(f"    [Error de Validacion] La linea no tiene 18 campos. Tiene {len(fields)}.")
        return None

    for i in range(1, 17):
        try:
            float(fields[i])
        except (ValueError, IndexError):
            print(f"    [Error de Validacion] El campo '{CSV_HEADER.split(',')[i]}' no es un numero valido o no existe.")
            return None
    
    if not re.search(r'\(\d{2}:\d{2}:\d{2}\)', fields[17]):
         print(f"    [Advertencia de Validacion] La justificacion para '{fields[0][:30]}...' no contiene un timestamp (HH:MM:SS).")

    return tuple(fields)

def insert_result(conn, data_tuple):
    try:
        cursor = conn.cursor()
        placeholders = ', '.join(['?'] * len(data_tuple))
        cursor.execute(f"INSERT OR IGNORE INTO {DB_TABLE} VALUES ({placeholders})", data_tuple)
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"    [Error de Base de Datos] No se pudo insertar el registro: {e}")
        return False

def export_db_to_csv():
    print("\nExportando resultados finales a CSV...")
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Clear the existing consolidated file before writing
        if os.path.exists(OUTPUT_FILE):
             os.remove(OUTPUT_FILE)
        
        cursor.execute(f"SELECT * FROM {DB_TABLE}")
        rows = cursor.fetchall()
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
            f.write(CSV_HEADER + '\n')
            for row in rows:
                justificacion = str(row[17])
                justificacion_escaped = justificacion.replace('"', '""')
                fields = list(map(str, row[:17])) + [f'\"{justificacion_escaped}\"']
                f.write(",".join(fields) + '\n')

        print(f"✔ Proceso completado. {len(rows)} registros guardados en {OUTPUT_FILE}")
    except sqlite3.Error as e:
        print(f"[Error] Ocurrió un error al exportar la base de datos: {e}")
    finally:
        if conn:
            conn.close()

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    setup_database()
    
    conn = sqlite3.connect(DB_FILE)
    
    all_vtt_files = sorted(glob.glob(os.path.join(INPUT_DIR, '*.vtt')))
    processed_names = get_processed_names(conn)
    files_to_process = [f for f in all_vtt_files if os.path.basename(f) not in processed_names]
    
    print(f"Archivos VTT en '{INPUT_DIR}': {len(all_vtt_files)}")
    print(f"Archivos ya procesados en la DB: {len(processed_names)}")
    print(f"Archivos pendientes de análisis: {len(files_to_process)}")

    for file_path in files_to_process:
        filename = os.path.basename(file_path)
        print(f"\nProcesando: {filename}")
        
        csv_line = gemini_analyze(filename)
        
        if not csv_line:
            print(f"    [Error] No se encontró o no se pudo leer el archivo de análisis para {filename}")
            continue

        print("    Validando resultado del modelo...")
        data_tuple = validate_and_parse_csv_line(csv_line)
        
        if data_tuple:
            print("    Resultado validado. Insertando en la base de datos...")
            if insert_result(conn, data_tuple):
                print(f"    ✔ '{filename}' guardado en la base de datos.")
            else:
                print(f"    [Advertencia] No se pudo guardar en la base de datos (puede que ya exista).")
        else:
            print(f"    [FALLO] El análisis para {filename} no pasó la validación y no será guardado.")

    conn.close()
    
    export_db_to_csv()

if __name__ == "__main__":
    main()

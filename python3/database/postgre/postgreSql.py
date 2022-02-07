import psycopg2
from psycopg2 import DatabaseError

try:
    myConectorDB = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='tu_password_db_postServer',
        database='nada_db'
    )

    print("Conexión exitosa.")
    mycur = myConectorDB.cursor()
    mycur.execute("SELECT version()")
    post_data = mycur.fetchone()
    print("Versión Postgre: {}".format(post_data))
    
    
    mycur.execute("SELECT * FROM table_name")
    filas_table_ = mycur.fetchall()
    for fila in filas_table_:
        print(fila)
except DatabaseError as e:
    print(f"Error de conexion: {e}")
finally:
    myConectorDB.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado cerrar programa.")

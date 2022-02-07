import sqlite3

try:
    myConectorDB = sqlite3.connect("db_prueba.db")#or prueba.sqlite3
    cursor = myConectorDB.cursor()
    cursor.execute("SELECT * FROM Academico_curso")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
except Exception as e:
    print(str(e))
finally:
    myConectorDB.close()

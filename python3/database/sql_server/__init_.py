import pyodbc

try:
    myConectorDB = pyodbc.connect('DRIVER={SQL Server};SERVER=CODSERVERAQUI;DATABASE=namedb;UID=xx;PWD=myPASWORD')

    print("Conexión exitosa.")
    cursor = myConectorDB.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print("Versión SQL Server: {}".format(row))
    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    myConectorDB.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")

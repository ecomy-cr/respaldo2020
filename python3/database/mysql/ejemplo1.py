import mysql.connector
from mysql.connector import Error

try:
    myConectorDB = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='django_api'
    )

    if myConectorDB.is_connected():
        print("Conexión exitosa.")
        infoServer = myConectorDB.get_server_info()
        print("Info del servidor: {}".format(infoServer))
        cursor = myConectorDB.cursor()
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
        print("Conectado a la base de datos: {}".format(row))
except Error as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    if myConectorDB.is_connected():
        myConectorDB.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

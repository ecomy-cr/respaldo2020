import mysql.connector
from mysql.connector import Error

"""
deben contar en el servidor con MysqlCLient, XAMPP buena opcion de serverLocal
python-mysqlconnector-PIP
para contar con puerto de mysql o MariaDB
"""

class MySQL_tools():
    
    def __init__(self):
        self.MyConnector = self._conexion_db()
        
    #pueden crear la Base de datos Madre directo con el Xampp y las tablas: O con el admin mysql que cuentes
    #creare mi database desde el phpadmin y las tablas tambien dejare el codigo con python para crearlas
    #con Python puro
    def _conexion_db(self):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='aqui_el_password_de_conexion_con_DBMysql',
                db='universidad2'
            )
            return conexion
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
            


    def _create_table(self,name):
        query = f'create table if not exists {name} (  )'
        mycursor = self.MyConnector.cursos()
        mycursor.execute(query)
        self.MyConnector.commit()
        
        '''
        CREATE TABLE `curso` (
            `ID` INT PRIMARY KEY AUTO_INCREMENT,
        `name` char(6) COLLATE utf8_unicode_ci NOT NULL,
        `grupo` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
        `ausencias` tinyint(2) UNSIGNED NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena a los estudiantes de la universidad simple database';
        '''


        
    
    def _ejecutar_consulta(self):
        pass
    
    def _crear_registro(self, array):
        if self.MyConnector.is_connected():
            try:
                cursor = self.MyConnector.cursor()
                query = "INSERT INTO estudiantes (name, grupo, ausencias) VALUES ('{0}', '{1}', {2})".format(array[0], array[1], array[2])
                cursor.execute(query)
                self.MyConnector.commit()
                print("Estudiante registrado!\n")
            except Error as e:
                print("Error al intentar la conexión: {0}".format(e))

    def _actualizar_registro(self, id, array):
        if self.MyConnector.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = f"UPDATE estudiantes SET name = '{array[0]}', grupo = {array[1]}, ausencias = {array[2]} WHERE id = {id}"
                cursor.execute(query)
                self.conexion.commit()
                print("¡Curso actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    
    def _eliminar_registro(self,id):
        if self.MyConnector.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = f"DELETE FROM estudiantes WHERE id = {id}"
                cursor.execute(query)
                self.conexion.commit()
                print("Estudiante eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def _listar_registro_s(self, id=None):
        if id:
            print('muestra solo un registro')
            if self.MyConnector.is_connected():
                try:
                    mycursor = self.MyConnector.cursor()
                    query = "SELECT * FROM registro where id={}".format(id)
                    mycursor.execute(query)
                    data = mycursor.fetchall()
                    return data
                except Error as e:
                    print("Error de conexion: {0}".format(e))


        else:
            print('Muestra todos los registros en db mysql')        
            if self.MyConnector.is_connected():
                try:
                    mycursor = self.MyConnector.cursor()
                    mycursor.execute("SELECT * FROM registro ORDER BY nombre ASC")
                    data = mycursor.fetchall()
                    return data
                except Error as e:
                    print("Error de conexion: {0}".format(e))


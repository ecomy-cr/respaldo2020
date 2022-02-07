from os import system
from random import random
import sqlite3
from sqlite3 import Error


class DB_sqlite_tools():
    def __init__(self):
        self.connector = self.mycon_sqlite()
        try:
            self._create_table_cursos()
        except Exception as e:
            print(str(e))
    def mycon_sqlite(self):
        try:
            con = sqlite3.connect('ecomycr.db')
            return con
        except Error:
            print(Error)
    def _create_table_cursos(self):
        try:
                
            mycur = self.connector.cursor()
            mycur.execute("""
                        CREATE TABLE IF NOT EXISTS 
                        cursos(id integer PRIMARY KEY, codigo text,  cursoname text, creditos text)
                        """)
            self.connector.commit()
        except:
            print('ha salido algo mal')

    def _ejecutar_(self, query, parametros = ()):
        try:
            self.cursor = self.connector.cursor()
            result = self.cursor.execute(query,parametros)
            self.connector.commit()
            return result
        except:
            return False
    
    def _ingresar_curso(self, cursoname, creditos):
        codigo = 'code random unique'
        curso = str(cursoname)
        creditos = str(creditos)
        try:
            if(len(curso) > 0 and len(creditos) > 0):
                query = "INSERT INTO cursos( codigo, cursoname, creditos) VALUES(?,?,?)"
                parametros = (codigo,cursoname ,creditos, )
                self._ejecutar_(query,parametros)
                print("curso nuevo insertado")
        except Exception as e:
            print('Error al insertar dato' + str(e))
    
    def _actualizar_curso(self,id, cursoname, creditos):
        try:
            if cursoname != '' and creditos!='':
                id = id
                if(id != 0):
                    cursoname=cursoname
                    creditos=creditos
                    query  = "UPDATE cursos SET cursoname=?,creditos=? WHERE id=?"
                    parametros = (cursoname,creditos,id)
                    self._ejecutar_(query,parametros)
                    print("Se ha actualizado con exito {}!".format(cursoname))
                else:
                    print("Se require un ID")
        except Exception as e:
            print(str(e))

    def _eliminar_curso(self,id):
        try:
            if(id != 0):
                query = "DELETE FROM cursos WHERE id=?"
                parametros = (id,)
                self._ejecutar_(query,parametros)
                print("Curso eliminado con exito!")
            else:
                print("Se require un ID")
        except:
            print('ha ocurrido un problema con el eliminado')
    
    def _listar_cursos(self, id=None):
        if id ==None:
            print('si')
            data = self._ejecutar_('Select * from cursos')
            for i in data:
                print(i)
        else:
            query = 'Select * from cursos where id={}'.format(id)
            data = self._ejecutar_(query)
            
            for i in data:
                print(i)






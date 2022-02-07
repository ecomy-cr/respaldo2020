import time
from os import system
from database_sqlite import DB_sqlite_tools
MyDB = DB_sqlite_tools()

print('Bienvenido al back de practica Cursos Academia')
print('Esta app es para crear, listar, actualizar y eliminar cursos de la academia')
print('Diviertete jugando en python')
print('')
system('clear')
print('')
print("=========================================")
print("\tCRUD CURSOS SQLITE")
print("=========================================")
print("\t[1] Insertar CURSO NUEVO")
print("\t[2] Listar CURSOS")
print("\t[3] Actualizar CURSO X")
print("\t[4] Eliminar CURSO X")
print("\t[5] Salir")
print("=========================================")
opcion = int(input("Seleccione una opción: "))
if opcion < 1 or opcion > 5:
    print("Opción incorrecta")
elif opcion == 5:
    continuar = False
    print("¡Chao!")
else:
    opcionCorrecta = True
    # se realiza codigo, UI falta while etc, se los dejo a su imaginacion

"""
try:
    if(resp == 1):
        # MyDB._ingresar_curso('Tec', '5')
        time.sleep(1)
        system("clear")
    elif (resp == 2):
        # MyDB._listar_cursos()

        time.sleep(1)
    elif (resp == 3):

        time.sleep(1)
        system("clear")
    elif (resp == 4):

        time.sleep(1)
        system("clear")
    else:
        print(['salir'])
        resp = 'salir'
except:
    print("Por favor, selecciona las respes correctas")
    system("clear")
    time.sleep(1)
"""
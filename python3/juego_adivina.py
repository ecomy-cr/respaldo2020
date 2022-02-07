# un juego de adivinar el numero
import random
import time
_intentos = 0
miNombre = input('Hola ¿Como te llamas?: ')

numero = random.randint(1,20) #escala del 1 al 20
print('Vamos a jugar ' + miNombre + ' estoy pensando un numero entre 1 al 20 cual es: ')
time.sleep(2)

while _intentos < 6:
    _myNum = float(input('Escribe el numero que creas: '))
    _myNum = int(_myNum)

    _intentos = _intentos + 1

    if _myNum < numero:
        print('tu _myNum es muy baja')
    if _myNum > numero:
        print('tu _myNum es muy alta')
    if _myNum == numero:
        break;

if _myNum == numero:
    _intentos = str(_intentos)
    print('Felicidades '+ miNombre+' has encontrado el numero en '+ _intentos +' intentos')

if _myNum != numero:
    numero = str(numero)
    print('Lastima, no has ganado, mi numero era:  '+ numero)
    
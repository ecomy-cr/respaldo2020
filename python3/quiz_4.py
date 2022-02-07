import time
import math
from math import *

from math import sin, cos


pi = 3.14
def numero_mayor():
    print('averiguando cual es el numero mayor')
    a=float(input('Ingresa numero 1: '))
    b=float(input('Ingresa numero 2: '))
    print('')

    if a>b:
        print('El primer numero es mayor')   
    elif a<b:
        print('El segundo numero es mayor')
    else:
        print('ambos numeros son iguales')

    print('Termina porque no esta en bucle solo se puede jugar una vez')
    time.sleep(2)

class libreria_math():
    def distancia_raiz():
        #calcular la distancia

        x1=float(input('Punto 1 de coordenada x'))
        y1=float(input('punto 1 de coordenada y'))
        x2=float(input('punto 2 de coordenada x'))
        y2=float(input('punto 2 de coordenada y'))

        dx=x2-x1
        dy=y2-y1
        distancia=sqrt(dx**2+dy**2)  # sqrt = raiz cuadrada
        print ('la distancia entre dos puntos es: ' + str(distancia))
    
    def log_math():
        #metodo log de math
        x=1.0
        while x < 100:
            print (x, '\t',log(x))
            x=x+1.0
    
    def circulo(pi):
        opcion=0
        while opcion !=4:
            print ('Escoge una opcion: ')
            print ('1-calcular el Diametro')
            print ('2-calcular el perimetro')
            print ('3-calcular el area')
            print ('4-salir')
            opcion=int(input('Seleccione una opcion 1-4: #'))
            radio=float(input('Cual es el radio: '))

            if opcion == 1:
                diametro = 2 * radio
                print ('el diametro es ',diametro)
            elif opcion ==2:
                perimetro=2*pi*radio
                print ('el perimetro es ',perimetro)
            elif opcion ==3:
                area=pi*radio**2
                print ('el area es ',area)
            elif opcion <0 or opcion >4:
                print ('solo hay cuatro opciones 1,2,3,4. tu has tecleado ',opcion)


    def informacion_estudio_math():
        a = 3//2;
        b = 3/2;
        c = 3 ** 2;

        # eponent begin from right side
        d = 2 ** 3 ** 2;

        # binary
        e = 0b0000 + 0b1;
        #octal
        f = 0o10 + 0o10;
        #hex
        g = 0x10 + 0x10;


        # predifend function
        print(abs(-3))
        print(float(3))
        print(float(3.2))
        print(float(3.2e10))
        # error: print(float('no es un numero'))
        print(int(3.2))
        print(str(3.2))
        print(bin(3))
        print(oct(3))
        print(hex(3))
        print(round(3.1))
        print(round(2.1415, 2)) #2.15 - the second param is for the decimals

        # string values
        print(ord('a'))
        print(ord('A'))
        # python3 unicode : print(ord('á'))

        print(math.sin(0))



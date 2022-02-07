import time
import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}*,;/-_¿?.¡!$<#>&+%="
combinaciones = 'hjgsjug786caynascasc.avdv;lksdovpsdl;;sdppsds90sd897sd89fhbsdhbjdv'
base = minus+mayus+numeros+simbolos+combinaciones

longitud = 15

def generar_nuevo_password():
    muestra = random.sample(base, longitud)
    print(muestra)
    password = "".join(muestra)
    print(password)
    password_encriptado = generate_password_hash(password)
    print(password_encriptado)
    print('')
    time.sleep(2)
    
    msj = {
        'password' : password,
        'encriptado' : password_encriptado,    
        }
    print('contrasena encriptada, y retornada como json')
    return msj

new_pass = generar_nuevo_password()
#se trabaja como json
import random

usuario_gana = 0
computadora_gana = 0

opciones = ["piedra", "papel", "tijera"]

while True:
    usuario_resp = input("escriba piedra/papel/tijera o precione Q para salir del juego: ").lower()
    if usuario_resp == "q":
        break

    if usuario_resp not in opciones:
        continue

    random_number = random.randint(0, 2)
    # piedra: 0, papel: 1, tijera: 2
    
    computadora_respuesta = opciones[random_number]
    print("La computadora: ", computadora_respuesta + ".")

    if usuario_resp == "piedra" and computadora_respuesta == "tijera":
        print("Usuario gana!")
        usuario_gana += 1

    elif usuario_resp == "papel" and computadora_respuesta == "piedra":
        print("Usuario gana!")
        usuario_gana += 1

    elif usuario_resp == "tijera" and computadora_respuesta == "papel":
        print("Usuario gana!")
        usuario_gana += 1

    else:
        print("Usuario pierde!")
        computadora_gana += 1

print("Usuario gano #", usuario_gana, " de veces.")
print("Computadora gano #", computadora_gana, " de veces.")
print("Chao gracias por jugar!")

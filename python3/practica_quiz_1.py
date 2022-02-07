import time
info = {
    'CreandoEnPython' : 'quiz_basico_1'
}
print(info)



start = input("Quieres realizar el quiz? s/n")

if start.lower() != "s":
    quit()

print("Saludos, iniciando el quiz...")

time.sleep(2)
resp_buenas = 0

answer = input("Capital de Costa Rica: ")
if answer.lower() == "san jose":
    print('Correct!')
    resp_buenas += 1
else:
    print("Incorrect!")

answer = input("Es el covid la nueva pandemia?")
if answer.lower() == "si":
    print('Correct!')
    resp_buenas += 1
else:
    print("Incorrect!")

answer = input("Que significa RAM")
if answer.lower() == "random access memory":
    print('Correct!')
    resp_buenas += 1
else:
    print("Incorrect!")

answer = input("Potencias del mundo")
if answer.lower() == "power supply":
    print('Correct!')
    resp_buenas += 1
else:
    print("Incorrect!")

print("Obtuviste " + str(resp_buenas) + " preguntas correctas!")
print("Obtuviste " + str((resp_buenas / 4) * 100) + "%.")
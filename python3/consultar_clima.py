import time
import requests

#informacion necesaria para la consulta al servidor del clima
api_kei_weather = 'aqi tu api key'
url_weather_api = 'http://api.openweathermap.org/'

API_KEY = api_kei_weather
BASE_URL = url_weather_api


#iniciando app
print('Iniciado aplicacion')
time.sleep(2)
print('')

#se solicita ciudad a consultar el clima
city = str(input("Nombre de la ciudad a consultar: "))

#realizo el url del api
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#obtengo el response
respuesta_response = requests.get(request_url)


#Manejo de errores
try:
    #si la consulta fue exitosa se obtiene un estado 200 HTTP
    if respuesta_response.status_code == 200:
        data = respuesta_response.json()
        
        
        weather = data['weather'][0]['description']
        
        temperature = round(data["main"]["temp"] - 273.15, 2)

        print("Clima:", weather)
        
        print("Temperatura:", temperature, "Celsius")
    
    else:
        print("...Algo ha salido mal con la consulta..")
except Exception as e:
    print('Error: ' + str(e))

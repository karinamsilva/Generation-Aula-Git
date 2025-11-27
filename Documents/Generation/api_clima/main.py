#Link API - Endpoint
#Link para metodos get/post
#https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m
# pip install requests - importação para requisições

import requests 
import matplotlib.pyplot as plt

#função para buscar clima 

def buscar_clima(latitude, longitude):
    #informar o endpoint
    weather_endpoint = "https://api.open-meteo.com/v1/forecast"
    param = {
        "latitude": latitude,
        "longitude":longitude,
        "hourly":"temperature_2m",
        "timezone":"America/Sao_Paulo"
    }
    resposta = requests.get(weather_endpoint,params=param)
    dados = resposta.json()

    return dados

lat = float(input('informe a latitude: '))
lon = float(input('informe a longitude: '))

dados = buscar_clima(lat,lon)
horas = dados['hourly']['time']
temperatura = dados['hourly']['temperature_2m']

plt.plot(horas,temperatura)
#plt.bar(horas,temperatura) - para criar um gráfico de coluna
# Cria um grafico onde informa o eixo X e o Y
plt.title('Temperatura por hora')

#para visualizar o grafico
plt.show()
import requests
from .config import *

#ejercicio 3, creo un input para cargar la moneda digital
moneda_cripto =input("Ingrese una criptomoneda conocida:").upper()

while moneda_cripto != "" and moneda_cripto.isalpha() == True:
  
    #invocar al metodo get con la url especifica
    r = requests.get( f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}' )

    respuesta = r.json()#la respuesta http en formato de diccionario

    #ejercicio 2, como capturo el error
    if r.status_code == 200:
        #ejercicio 1, como capturamos el rate
        print( "{:,.2f}€".format( respuesta['rate']) )#1903.90€
        break
    else:
        print(respuesta['error'])

    moneda_cripto =input("Ingrese una criptomoneda conocida:").upper()


"""
print("codigo http de respuesta:",r.status_code)
print("cabecera:",r.headers['content-type'])
print("encoding:",r.encoding)
print("respuesta en string:",r.text)
print(type(r.text))
print("respuesta en json:",r.json())
print(type(r.json()))
"""
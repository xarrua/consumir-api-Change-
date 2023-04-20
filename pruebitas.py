"""
respuesta = {'time': '2023-04-17T19:57:50.0000000Z',
              'asset_id_base': 'BTC',
                'asset_id_quote': 'EUR',
                  'rate': 26999.55580795389}

print("Esto es time: ",respuesta['time'])
print("Esto es base: ",respuesta['asset_id_base'])
print("Esto es quote: ",respuesta['asset_id_quote'])
print("Esto es rate: ",respuesta['rate'])


respuesta2={ 'error': "You requested specific single item that we don't have at this moment."}

print(respuesta2['error'])

numero = "sds"
print(numero.isalpha())
"""

respuesta = {
    'dato1':"Jose",
    'dato2':"Maria"
}

print(respuesta['dato1'])
# Aplicación de consulta de valor actual de criptos

Programa hecho en python para recuperar el valor en euros de una criptomoneda desde www.coinapi.io

## Instalación
- Obtener una apiKey en www.coinapi.io

- Renombrar el fichero 'config_template.py' a 'config.py' y en el agregar tu apikey obtenida en la variable 'apikey'

```
APIKEY="4d5f4d5f45df45d4f5d4fd5"
```

## Instalación de dependencias
- crear un entorno de python 
```
py -m venv entorno
```

- Activate el entorno y instalar el requirements
```
pip install -r requirements.txt
```
- Utiliza la libreria de pytest y requests
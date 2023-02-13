import requests

# URL de la API de NASA
url = "https://api.nasa.gov/planetary/apod"

# Parámetros de la API, incluyendo la clave de API
params = {
    "api_key": "YOUR_API_KEY_HERE",
    "count": 5
}

# Hacer la solicitud a la API
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Cargar los datos de la respuesta en un diccionario de Python
    data = response.json()

    # Recorrer los datos y mostrar algunos detalles
    for item in data:
        print("Title:", item["title"])
        print("Date:", item["date"])
        print("URL:", item["url"])
        print("\n")
else:
    # Mostrar un mensaje de error si la solicitud no fue exitosa
    print("Error:", response.status_code)
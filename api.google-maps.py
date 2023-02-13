import requests

# API Key de Google Maps
api_key = "<tu_api_key>"

# URL de la API de Google Maps
url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=<nombre_del_lugar>&inputtype=textquery&fields=name,formatted_address,geometry&key={api_key}"

# Hacemos una petici�n GET a la API de Google Maps
response = requests.get(url)

# Verificamos si la respuesta es exitosa
if response.status_code == 200:
    # Convertimos la respuesta a formato JSON
    place_data = response.json()
    print("Nombre:", place_data["candidates"][0]["name"])
    print("Direcci�n:", place_data["candidates"][0]["formatted_address"])
    print("Latitud:", place_data["candidates"][0]["geometry"]["location"]["lat"])
    print("Longitud:", place_data["candidates"][0]["geometry"]["location"]["lng"])
else:
    # Si la respuesta no es exitosa, imprimimos el c�digo de estado de la respuesta
    print("No se pudo obtener informaci�n sobre el lugar. C�digo de estado:", response.status_code)
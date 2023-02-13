import requests

# Hacemos una petici�n GET a la API de GitHub para obtener informaci�n sobre un usuario
url = "https://api.github.com/users/<username>"
response = requests.get(url)

# Verificamos si la respuesta es exitosa
if response.status_code == 200:
    # Convertimos la respuesta a formato JSON
    user_data = response.json()
    print("Nombre de usuario:", user_data["login"])
    print("Nombre completo:", user_data["name"])
    print("Ubicaci�n:", user_data["location"])
    print("N�mero de seguidores:", user_data["followers"])
else:
    # Si la respuesta no es exitosa, imprimimos el c�digo de estado de la respuesta
    print("No se pudo obtener informaci�n sobre el usuario. C�digo de estado:", response.status_code)
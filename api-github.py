import requests

# Hacemos una petición GET a la API de GitHub para obtener información sobre un usuario
url = "https://api.github.com/users/<username>"
response = requests.get(url)

# Verificamos si la respuesta es exitosa
if response.status_code == 200:
    # Convertimos la respuesta a formato JSON
    user_data = response.json()
    print("Nombre de usuario:", user_data["login"])
    print("Nombre completo:", user_data["name"])
    print("Ubicación:", user_data["location"])
    print("Número de seguidores:", user_data["followers"])
else:
    # Si la respuesta no es exitosa, imprimimos el código de estado de la respuesta
    print("No se pudo obtener información sobre el usuario. Código de estado:", response.status_code)
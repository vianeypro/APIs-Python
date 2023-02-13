import requests
import json

# Obtener un token de acceso v�lido de Facebook
access_token = "YOUR_ACCESS_TOKEN"

# Define la versi�n de la API de Facebook que deseas utilizar
version = "7.0"

# Especifica la p�gina que deseas obtener
page_id = "YOUR_PAGE_ID"

# Realiza una solicitud a la API de Facebook
url = f"https://graph.facebook.com/v{version}/{page_id}?fields=id,name,likes&access_token={access_token}"
response = requests.get(url)

# Procesa la respuesta
data = json.loads(response.text)

# Imprime los datos
print(data)
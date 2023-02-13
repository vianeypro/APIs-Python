import requests

# API key de OpenWeatherMap
api_key = "your_api_key_here"

# Nombre de la ciudad
city = "Mexico"

# Realizar una solicitud a la API de OpenWeatherMap
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear la respuesta JSON
    data = response.json()
    
    # Obtener la temperatura en grados Celsius
    temperature = data["main"]["temp"] - 273.15
    
    # Obtener la descripción del tiempo
    weather_description = data["weather"][0]["description"]
    
    # Mostrar la temperatura y la descripción del tiempo en un formato legible
    print(f"La temperatura actual en {city} es de {temperature:.2f}°C y el clima es {weather_description}.")
else:
    # Mostrar un mensaje de error si la solicitud no fue exitosa
    print("Hubo un problema al obtener los datos del clima.")
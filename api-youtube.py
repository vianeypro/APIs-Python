from googleapiclient.discovery import build

# Crea una instancia de la API de YouTube
youtube = build("youtube", "v3", developerKey="YOUR_API_KEY")

# Realiza una llamada a la API para obtener informaci�n sobre un video espec�fico
request = youtube.videos().list(part="snippet,contentDetails,statistics", id="video_id")
response = request.execute()

# Imprime la respuesta
print(response)
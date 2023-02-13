import tweepy

# Autenticación con las claves de API y secreto de API de Twitter
auth = tweepy.OAuthHandler("API_KEY", "API_SECRET_KEY")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Conectarse a la API de Twitter
api = tweepy.API(auth)

# Publicar un tweet
api.update_status("Hello, World!")
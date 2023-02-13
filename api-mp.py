import requests
import json

# Configura tus credenciales de MercadoPago
access_token = "YOUR_ACCESS_TOKEN"

# Define la informaci�n de la transacci�n
payment_data = {
    "transaction_amount": 100,
    "token": "YOUR_CARD_TOKEN",
    "description": "Compra de productos",
    "installments": 1,
    "payment_method_id": "visa",
    "payer": {
        "email": "payer@email.com"
    }
}

# Realiza la transacci�n
response = requests.post(
    "https://api.mercadopago.com/v1/payments?access_token=" + access_token,
    json=payment_data
)

# Verifica el resultado de la transacci�n
if response.status_code == 201:
    payment = json.loads(response.text)
    print("Transacci�n exitosa! ID:", payment["id"])
else:
    print("Error en la transacci�n:", response.text)
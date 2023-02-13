import requests
import json

# Configura tus credenciales de PayPal
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Obtiene un token de acceso
auth = requests.post(
    "https://api.sandbox.paypal.com/v1/oauth2/token",
    headers={
        "Accept": "application/json",
        "Accept-Language": "en_US",
        "Content-Type": "application/x-www-form-urlencoded"
    },
    data={
        "grant_type": "client_credentials"
    },
    auth=(client_id, client_secret)
)

# Verifica el resultado de la autenticación
if auth.status_code == 200:
    access_token = json.loads(auth.text)["access_token"]
else:
    print("Error en la autenticación:", auth.text)
    exit()

# Define la información de la transacción
payment_data = {
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"
    },
    "transactions": [
        {
            "amount": {
                "total": "100.00",
                "currency": "USD"
            },
            "description": "Compra de productos"
        }
    ],
    "redirect_urls": {
        "return_url": "http://localhost:3000/success",
        "cancel_url": "http://localhost:3000/cancel"
    }
}

# Realiza la transacción
payment = requests.post(
    "https://api.sandbox.paypal.com/v1/payments/payment",
    headers={
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    },
    json=payment_data
)

# Verifica el resultado de la transacción
if payment.status_code == 201:
    payment = json.loads(payment.text)
    print("Transacción exitosa! ID:", payment["id"])
else:
    print("Error en la transacción:", payment.text)
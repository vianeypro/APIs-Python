import requests
import json

# Replace {client_id} and {client_secret} with your own values.
data = {
    'client_id': '{client_id}',
    'scope': 'openid profile User.Read Calendars.Read',
    'redirect_uri': 'http://localhost:8000',
    'response_type': 'code',
    'prompt': 'consent'
}

# Request an authorization code.
response = requests.get('https://login.microsoftonline.com/common/oauth2/v2.0/authorize', params=data)

# Extract the authorization code.
code = input("Enter the authorization code: ")

# Get the access token.
data = {
    'client_id': '{client_id}',
    'redirect_uri': 'http://localhost:8000',
    'client_secret': '{client_secret}',
    'code': code,
    'grant_type': 'authorization_code'
}

response = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data)

# Extract the access token.
access_token = response.json()['access_token']

# Get the events from the calendar.
response = requests.get('https://outlook.office.com/api/v2.0/me/events', headers={'Authorization': f'Bearer {access_token}'})

# Print the events.
events = response.json()['value']
for event in events:
    print(event['subject'], event['start']['dateTime'], event['end']['dateTime'])
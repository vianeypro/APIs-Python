import base64
from email.mime.text import MIMEText
import os
from googleapiclient.discovery import build

def send_email(to, body):
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = 'Test Email'
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'Email was sent to "{to}" with Email Id: {send_message["id"]}')
    except Exception as error:
        print(F'An error occurred: {error}')

send_email(to='recipient_email@example.com', body='Hello, this is a test email sent using the Gmail API.')
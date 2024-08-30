import requests
from django.conf import settings

def send_telegram_message(name, email, message):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f'https://api.telegram.org/bot7527667648:AAEcY0hyRZmw7wUO5B-eqY1Xnw5Pl5n-lr4/sendMessage'
    text = (f"New contact form submission from {name} ({email}):\n\n{message}")
    data = {
        'chat_id': chat_id,
        'text': text,
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")

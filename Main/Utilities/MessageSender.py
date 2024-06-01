import requests


def send_telegram_message(token, recipient, msg):
    """
    Send a message to a Telegram user using a bot.

    :param token: The token of the Telegram bot.
    :param recipient: The chat ID of the recipient.
    :param msg: The message to send.
    """
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': recipient,
        'text': msg
    }
    response = None
    for i in range(10):
        response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")


bot_token = '7438234940:AAHllO2wm56vUpuw14RrXXpwTMbP_FTLP_I'
chat_id = '6397942332'
message = 'Hello, this is a test message!'

send_telegram_message(bot_token, chat_id, message)


def get_user_id(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    print(response.json())

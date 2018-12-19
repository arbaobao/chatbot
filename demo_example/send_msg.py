import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = 'EAAQ1FLq35agBALfsp66dsZB1Osvbjc13uD4Ag4nRek3XMMNWZC0xPZCKv1jrgh6Syb1Kcrg3s02r86pnbzjNsh78rKZCo10veBZAqDL9zEEmioVKpCkAV5Btr66PP4UvH3ZA9YrIdiUiZAIePFXnbRk0eMnRpMgnwVJAC5MwYJbkAZDZD'

VERIFY_TOKEN = '9487'


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text

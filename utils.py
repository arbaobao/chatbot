import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = 'EAAQ1FLq35agBAHeLZA3dApZAcWZAiSi4zouZByH0ddKFZCHt9iMRuYdaUA1CgGJev14L1m5SCKYsnmBWMS5LGbg4GWhM4gvxSSqgEImC8F46HN4YHpMKio9UnPTrXOeKThCBBzivENG7tZB2DJz0Cizqac1OGulxlSLhMdrmLc3wZDZD'



def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""

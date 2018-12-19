from bottle import route, run, request


VERIFY_TOKEN = '9487'

ACCESS_TOKEN = 'EAAQ1FLq35agBALfsp66dsZB1Osvbjc13uD4Ag4nRek3XMMNWZC0xPZCKv1jrgh6Syb1Kcrg3s02r86pnbzjNsh78rKZCo10veBZAqDL9zEEmioVKpCkAV5Btr66PP4UvH3ZA9YrIdiUiZAIePFXnbRk0eMnRpMgnwVJAC5MwYJbkAZDZD'


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

run(host="localhost", port=5000, debug=True)

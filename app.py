from bottle import route, run, request, abort, static_file

from fsm import TocMachine

ACCESS_TOKEN = 'EAAQ1FLq35agBALfsp66dsZB1Osvbjc13uD4Ag4nRek3XMMNWZC0xPZCKv1jrgh6Syb1Kcrg3s02r86pnbzjNsh78rKZCo10veBZAqDL9zEEmioVKpCkAV5Btr66PP4UvH3ZA9YrIdiUiZAIePFXnbRk0eMnRpMgnwVJAC5MwYJbkAZDZD'
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']

machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
       # {
       #     'trigger': 'advance',
       #     'source': 'user',
       #     'dest': 'state2',
       #     'conditions': 'is_going_to_state2'
       # },
       # {
       #     'trigger': 'advance',
       #     'source': 'user',
       #     'dest': 'state3',
       #     'conditions': 'is_going_to_state3'
       # },
       # {
        #    'trigger':'advance',
        #    'source': 'user',
        #    'dest': 'state4',
        #    'conditions': 'is_going_to_state4'
        #},
        {
            'trigger': 'go_back',
            'source': [
                'state2',
                'state3',
                'state4'
            ],
            'dest': 'user'
        },
        {
            'trigger':'go_state1',
            'source':'state1',
            'dest':'state1'
        },
        {
            'trigger':'advance',
            'source':'state1',
            'dest':'state2',
            'conditions':'state1_to_state2'
        },
        {
            'trigger':'advance',
            'source':'state1',
            'dest':'state3',
            'conditions':'state1_to_state3'
        },
        {
            'trigger':'advance',
            'source':'state1',
            'dest':'state4',
            'conditions':'state1_to_state4'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)

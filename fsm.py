from transitions.extensions import GraphMachine

from utils import send_text_message
ACCESS_TOKEN = 'EAAQ1FLq35agBALfsp66dsZB1Osvbjc13uD4Ag4nRek3XMMNWZC0xPZCKv1jrgh6Syb1Kcrg3s02r86pnbzjNsh78rKZCo10veBZAqDL9zEEmioVKpCkAV5Btr66PP4UvH3ZA9YrIdiUiZAIePFXnbRk0eMnRpMgnwVJAC5MwYJbkAZDZD'

VERIFY_TOKEN = '9487'

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'list team'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'brothers'
        return False
    
    def is_going_to_state3(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'lions'
        return False
        
    def is_going_to_state4(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'lamigo'
        return False

    def state1_to_state2(self,event):
        print("hi")

        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'brothers'
        return False

    def state1_to_state3(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower()== 'lions'
        return False
    
    def state1_to_state4(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'lamigo'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")
        
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "you can key in 'lions' 'brothers' 'lamigo' to search their website~   ")
        self.go_state1()        



    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "here is the website of brothers:https://www.brothers.tw/")
        self.go_back()

    def on_enter_state3(self,event):
        print("I'm entering state3")        

        sender_id = event['sender']['id']
        send_text_message(sender_id, "here is the website of lions:https://www.uni-lions.com.tw/")
        self.go_back()

    def on_enter_state4(self,event):

        print("I'm entering state4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "here is the website of lamigo:https://www.lamigo-monkeys.com.tw/")
        self.go_back()


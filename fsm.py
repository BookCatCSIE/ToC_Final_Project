from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, push_text_message

import random


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        push_text_message(self.push_token, "輸入數字 : 1.御主抽從者 2.抽御神籤") ###

    def is_going_to_state1(self, event):
        text = event.message.text
        #return text.lower() == "go to state1"  #檢查input text : "go to state1" ?
        return text.lower() == "1"

    def is_going_to_state2(self, event):
        text = event.message.text
        #return text.lower() == "go to state2"  #檢查input text : "go to state2" ?
        return text.lower() == "2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state1")  #依state1產生 output : "Trigger state1" ?
        rand = random.randint(0,2)
        img_url=""
        if rand==0:
            img_url = "https://imgur.com/76qpcCc"
        elif rand==1:
            img_url = "https://imgur.com/eVtNnum"
        elif rand==2:
            img_url = "https://imgur.com/9iGL2iK"

        send_image_url(reply_token, img_url)
        self.go_back()                            # state1產生output後自動回user state

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state2")  #依state2產生 output : "Trigger state2" ?
        rand = random.randint(0,2)
        text=""
        if rand==0:
            text = "大吉"
        elif rand==1:
            text = "小吉"
        elif rand==2:
            text = "末吉"

        send_text_message(reply_token, text)
        self.go_back()                            # state2產生output後自動回user state

    def on_exit_state2(self):
        print("Leaving state2")

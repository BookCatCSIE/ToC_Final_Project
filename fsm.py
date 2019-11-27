from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, push_text_message

import random

from linebot.models import StickerSendMessage


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        #push_text_message(self.push_token, "輸入數字 : 1.御主抽從者 2.抽御神籤") ###

    def is_going_to_state1(self, event):
        text = event.message.text
        #return text.lower() == "go to state1"  #檢查input text : "go to state1" ?
        #return text.lower() == "1"
        return text.startswith('1')

    def is_going_to_state2(self, event):
        text = event.message.text
        #return text.lower() == "go to state2"  #檢查input text : "go to state2" ?
        #return text.lower() == "2"
        return text.startswith('2')

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state1")  #依state1產生 output : "Trigger state1" ?
        text = event.message.text

        if text.lower() == "1-1":
            img_url=''
            rand = random.randint(0,13)
            if rand==0:
                img_url = 'https://imgur.com/76qpcCc.png'
            elif rand==1:
                img_url = 'https://imgur.com/Hbla4WE.png'
            elif rand==2:
                img_url = 'https://imgur.com/EPnjFrF.png'
            elif rand==3:
                img_url = 'https://imgur.com/FzXrxF4.png'
            elif rand==4:
                img_url = 'https://imgur.com/VHKV9fh.png'
            elif rand==5:
                img_url = 'https://imgur.com/a1OoV4s.png'
            elif rand==6:
                img_url = 'https://imgur.com/5HWQuH0.png'
            elif rand==7:
                img_url = 'https://imgur.com/C6pN6dN.png'
            elif rand==8:
                img_url = 'https://imgur.com/AGcLk2B.png'
            elif rand==9:
                img_url = 'https://imgur.com/8v09XgC.png'
            elif rand==10:
                img_url = 'https://imgur.com/8ICBiAr.png'
            elif rand==11:
                img_url = 'https://imgur.com/yAYDNVu.png'
            elif rand==12:
                img_url = 'https://imgur.com/R1w37BY.png'
            elif rand==13:
                img_url = 'https://imgur.com/8MGq627.png'

            send_image_url(reply_token, img_url)

        elif text.lower() == "1-2":
            text = ""
            rand = random.randint(0,7)
            if rand==0:
                text = "大吉"
            elif rand==1:
                text = "中吉"
            elif rand==2:
                text = "小吉"
            elif rand==3:
                text = "吉"
            elif rand==4:
                text = "半吉"
            elif rand==5:
                text = "末吉"
            elif rand==6:
                text = "末小吉"
            elif rand==7:
                text = "小凶"

            send_text_message(reply_token, text)

        elif text.lower() == "1-3":
            rand1 = random.randint(1,3)
            rand2 = random.randint(1,5)
            p=''
            s=''
            if rand1==1:
                p='1'
            elif rand1==2:
                p='2'
            elif rand1==3:
                p='3'

            if rand2==1:
                s='1'
            elif rand2==2:
                s='2'
            elif rand2==3:
                s='3'
            elif rand2==4:
                s='4'
            elif rand2==5:
                s='5'   

            message = StickerSendMessage(package_id=p,sticker_id=s)
            line_bot_api = LineBotApi("Rm8xX4VBF4waMmWihvF6oqsbNhEHfJrV5qgh2jsU5u0Nh73SmBLwb8IOLMWCCpCsWEzSLx7UoMQugiEEgRV/iQPcclFWMCaJ1RXO8nkftlCih+ndu/BRrRPCnAjWX89r4CEGG64fr4ItC76iIwpqdwdB04t89/1O/w1cDnyilFU=")
            line_bot_api.reply_message(reply_token, message)

        else:
            push_text_message(event.push_token, "fffffffffff") ###
            send_text_message(reply_token, "輸入數字 : 1-1.御主抽從者 1-2.參拜者抽御神籤 2.")

        '''
        rand = random.randint(0,21)
        img_url=''
        text=""
        if rand==0:
            img_url = 'https://imgur.com/76qpcCc.png'
        elif rand==1:
            img_url = 'https://imgur.com/Hbla4WE.png'
        elif rand==2:
            img_url = 'https://imgur.com/EPnjFrF.png'
        elif rand==3:
            img_url = 'https://imgur.com/FzXrxF4.png'
        elif rand==4:
            img_url = 'https://imgur.com/VHKV9fh.png'
        elif rand==5:
            img_url = 'https://imgur.com/a1OoV4s.png'
        elif rand==6:
            img_url = 'https://imgur.com/5HWQuH0.png'
        elif rand==7:
            img_url = 'https://imgur.com/C6pN6dN.png'
        elif rand==8:
            img_url = 'https://imgur.com/AGcLk2B.png'
        elif rand==9:
            img_url = 'https://imgur.com/8v09XgC.png'
        elif rand==10:
            img_url = 'https://imgur.com/8ICBiAr.png'
        elif rand==11:
            img_url = 'https://imgur.com/yAYDNVu.png'
        elif rand==12:
            img_url = 'https://imgur.com/R1w37BY.png'
        elif rand==13:
            img_url = 'https://imgur.com/8MGq627.png'
        elif rand==14:
            text = "大吉"
        elif rand==15:
            text = "中吉"
        elif rand==16:
            text = "小吉"
        elif rand==17:
            text = "吉"
        elif rand==18:
            text = "半吉"
        elif rand==19:
            text = "末吉"
        elif rand==20:
            text = "末小吉"
        elif rand==21:
            text = "小凶"

        if rand<=13:
            send_image_url(reply_token, img_url)
        else:
            send_text_message(reply_token, text)
        '''

        self.go_back()                            # state1產生output後自動回user state

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state2")  #依state2產生 output : "Trigger state2" ?
        text="111"
        send_text_message(reply_token, text)
        self.go_back()                            # state2產生output後自動回user state

    def on_exit_state2(self):
        print("Leaving state2")

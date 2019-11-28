from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, push_text_message, send_sticker

import random

from linebot.models import StickerSendMessage

import crawler


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
            sticker_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 100, 101, 102, 103, 104, 105, 106,
                    107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
                    126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 401, 402]
            index_id = random.randint(0, len(sticker_ids) - 1)
            sticker_id = str(sticker_ids[index_id])

            message = StickerSendMessage(package_id='1',sticker_id=sticker_id)
            send_sticker(reply_token, message)

        else:
            send_text_message(reply_token, "輸入數字 :  1-1.御主抽從者  1-2.參拜者抽御神籤  1-3.隨機貼圖  2.")

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
        #if text.lower() == "2-1":
        #    text=
        #send_text_message(reply_token, text)
        text=event.message.text[1:]
        img_url = get_image_link(text)
        send_image_url(reply_token, img_url)

        self.go_back()                            # state2產生output後自動回user state

    def on_exit_state2(self):
        print("Leaving state2")

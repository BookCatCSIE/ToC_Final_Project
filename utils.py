import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("Rm8xX4VBF4waMmWihvF6oqsbNhEHfJrV5qgh2jsU5u0Nh73SmBLwb8IOLMWCCpCsWEzSLx7UoMQugiEEgRV/iQPcclFWMCaJ1RXO8nkftlCih+ndu/BRrRPCnAjWX89r4CEGG64fr4ItC76iIwpqdwdB04t89/1O/w1cDnyilFU=", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""

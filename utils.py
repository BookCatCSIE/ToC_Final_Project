import os

from linebot import LineBotApi, WebhookParser
#from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import * #----------------------------------------------------


#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
channel_access_token = os.getenv("", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi("")
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi("")
    line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=img_url,preview_image_url=img_url))

    return "OK"


def push_text_message(push_token, text):
    line_bot_api = LineBotApi("")
    line_bot_api.push_message(push_token, TextSendMessage(text=text))

    return "OK"

def send_sticker(reply_token, message):
    line_bot_api = LineBotApi("")
    line_bot_api.reply_message(reply_token, message)

    return "OK"





"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""

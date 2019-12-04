import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
#from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import * #----------------------------------------------------

from fsm import TocMachine
from utils import send_text_message, send_image_url, push_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "state1", "state2"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {"trigger": "go_back", "source": ["state1", "state2"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
#channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
#channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
channel_secret = os.getenv("73a94799bad3cfacb1e3dc5d63fb6a48", None)
channel_access_token = os.getenv("Rm8xX4VBF4waMmWihvF6oqsbNhEHfJrV5qgh2jsU5u0Nh73SmBLwb8IOLMWCCpCsWEzSLx7UoMQugiEEgRV/iQPcclFWMCaJ1RXO8nkftlCih+ndu/BRrRPCnAjWX89r4CEGG64fr4ItC76iIwpqdwdB04t89/1O/w1cDnyilFU=", None)

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    #sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    #sys.exit(1)

#line_bot_api = LineBotApi(channel_access_token)
#parser = WebhookParser(channel_secret)
line_bot_api = LineBotApi("Rm8xX4VBF4waMmWihvF6oqsbNhEHfJrV5qgh2jsU5u0Nh73SmBLwb8IOLMWCCpCsWEzSLx7UoMQugiEEgRV/iQPcclFWMCaJ1RXO8nkftlCih+ndu/BRrRPCnAjWX89r4CEGG64fr4ItC76iIwpqdwdB04t89/1O/w1cDnyilFU=")
parser = WebhookParser("73a94799bad3cfacb1e3dc5d63fb6a48")

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        #line_bot_api.reply_message(
        #    event.reply_token, TextSendMessage(text=event.message.text)
        #)
        #push_text_message(self.push_token, "輸入數字 : 1.御主抽從者 2.抽御神籤") ###

        response = machine.advance(event)
        if response == False:
            #send_text_message(event.reply_token, "Not Entering any State")
            send_text_message(event.reply_token, "輸入數字 :  1-1.御主抽從者  1-2.參拜者抽御神籤  1-3.隨機貼圖  2.爬蟲--科技新報 ")
            # input不符時產生的output

    return "OK"

# 回覆訊息的地方?
@app.route("/webhook", methods=["POST"])
# def webhook_handler():
    # signature = request.headers["X-Line-Signature"]
    # # get request body as text
    # body = request.get_data(as_text=True)
    # app.logger.info(f"Request body: {body}")

    # # parse webhook body
    # try:
        # events = parser.parse(body, signature)
    # except InvalidSignatureError:
        # abort(400)

    # # if event is MessageEvent and message is TextMessage, then echo text
    # for event in events:
        # if not isinstance(event, MessageEvent):
            # continue
        # if not isinstance(event.message, TextMessage):
            # continue
        # if not isinstance(event.message.text, str):
            # continue
        # print(f"\nFSM STATE: {machine.state}")
        # print(f"REQUEST BODY: \n{body}")
        # response = machine.advance(event)
        # if response == False:
            # send_text_message(event.reply_token, "Not Entering any State")
            # # input不符時產生的output

    # return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
    show_fsm()
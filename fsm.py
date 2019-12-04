from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, push_text_message, send_sticker

import random

from linebot.models import StickerSendMessage

#-----------------------------------------------------------
import requests
import re
from bs4 import BeautifulSoup
from imgurpython import ImgurClient

def technews():
    target_url = 'https://technews.tw/'
    print('Start parsing movie ...')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for index, data in enumerate(soup.select('article div h1.entry-title a')):
        if index == 12:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content


def ptt_beauty():
    rs = requests.session()
    res = rs.get('https://www.ptt.cc/bbs/Beauty/index.html', verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_page_url = soup.select('.btn.wide')[1]['href']
    start_page = get_page_number(all_page_url)
    page_term = 2  # crawler count
    push_rate = 10  # 推文
    index_list = []
    article_list = []

    for page in range(start_page, start_page - page_term, -1):
        page_url = 'https://www.ptt.cc/bbs/Beauty/index{}.html'.format(page)
        index_list.append(page_url)

    # 抓取 文章標題 網址 推文數
    while index_list:
        index = index_list.pop(0)
        res = rs.get(index, verify=False)
        # 如網頁忙線中,則先將網頁加入 index_list 並休息1秒後再連接
        if res.status_code != 200:
            index_list.append(index)
            # print u'error_URL:',index
            # time.sleep(1)
        else:
            article_list = craw_page(res, push_rate)
            # print u'OK_URL:', index
            # time.sleep(0.05)
    content = ''
    for article in article_list:
        data = '[{} push] {}\n{}\n\n'.format(article.get('rate', None), article.get('title', None),article.get('url', None))
        content += data
    return content


def oil_price():
    target_url = 'https://gas.goodlife.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('#main')[0].text.replace('\n', '').split('(')[0]
    gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ', '')
    cpc = soup.select('#cpc')[0].text.replace(' ', '')
    content = '{}\n{}{}'.format(title, gas_price, cpc)
    return content



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
            send_text_message(reply_token, "輸入數字 :  1-1.御主抽從者  1-2.參拜者抽御神籤  1-3.隨機貼圖  2-1.爬蟲--科技新報  2-2.爬蟲--PTT表特版  2-3.爬蟲--油價 ")

        self.go_back()                            # state1產生output後自動回user state

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token

        if text.lower() == "2-1":
            message = technews()
            send_text_message(reply_token, message)

        elif text.lower() == "2-2":
            message = ptt_beauty()
            send_text_message(reply_token, message)

        elif text.lower() == "2-3":
            message = oil_price()
            send_text_message(reply_token, message)

        else:
            send_text_message(reply_token, "輸入數字 :  1-1.御主抽從者  1-2.參拜者抽御神籤  1-3.隨機貼圖  2-1.爬蟲--科技新報  2-2.爬蟲--PTT表特版  2-3.爬蟲--油價 ")

        self.go_back()                            # state2產生output後自動回user state

    def on_exit_state2(self):
        print("Leaving state2")

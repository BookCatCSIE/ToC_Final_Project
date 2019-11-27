import requests 
from beautifulsoup4 import BeautifulSoup
from urllib3.request import urlretrieve

def movie():
    target_url = 'https://movies.yahoo.com.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('div.movielist_info h1 a')):
        if index == 20:
            return content       
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)
    return content


#target_url -> 要爬的網址
#soup = BeautifulSoup(res.text, 'html.parser') -> 讀入網頁
#select('div.movielist_info h1 a') -> 找Tag
#Tag怎麼找呢?  找你想要的內容，按右鍵 > "檢查"就可找了 ex: div.movielist_info > h1 > a


#if event.message.text == "最新電影":
#        a=movie()
#        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=a))
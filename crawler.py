import json
from selenium import webdriver
GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
def get_image_link(search_query):
    img_urls = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    #chrome_options.binary_location = GOOGLE_CHROME_PATH
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=CHROMEDRIVER_PATH)
#    driver = webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver')
    t = search_query[:-4]+'餐點價格'
    url = 'https://www.google.com/search?q=' + t 
    driver.get(url)
    imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta notranslate")]')
    count = 0
    for img in imges:
        img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
        print(str(count)+'--->'+str(img_url))
        if img_url.startswith('https') == False:
            continue
        img_urls.append(img_url)
        if count > 1:
            break
        count = count + 1
    driver.quit()
    return img_urls
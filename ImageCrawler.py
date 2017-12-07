#Download image from imgur.com
import requests
from bs4 import BeautifulSoup
import shutil

def ImageCrawler(url):
    response = requests.get('https://www.ptt.cc/bbs/Beauty/M.1512544511.A.064.html')
    soup = BeautifulSoup(response.text,"html.parser")

    for item in soup.find_all('a'):

        if item.text.find('imgur.com')==10:
            url = item.text
            fname = url.split('/')[-1]
            response2 = requests.get(url, stream=True)
            f = open('d:\jeffc_chao\Desktop\python\PTT_Crawler\img\\'+fname, 'wb')
            shutil.copyfileobj(response2.raw, f)
            f.close()
            del response2

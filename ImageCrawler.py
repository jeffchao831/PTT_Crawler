#Download image from imgur.com
import shutil
import sys
import requests
from bs4 import BeautifulSoup


def image_crawler(url):
    """Crawling images from main content of article."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('title').text

    if title.find('[正妹]') != -1:
            #Delete image url in push content
        for item in soup.find_all('div', {'class':'push'}):
            if item.a:
                item.a.decompose()

        for item in soup.find_all('a'):
            if item.text.find('imgur.com') != -1:
                url = item.text
                fname = url.split('/')[-1]
                response2 = requests.get(url, stream=True)
                img = open('d:\\jeffc_chao\\Desktop\\python\\PTT_Crawler\\img\\'+fname, 'wb')
                shutil.copyfileobj(response2.raw, img)
                img.close()
                del response2

def main(argv):
    image_crawler('https://www.ptt.cc/bbs/Beauty/M.1512612132.A.309.html')

if __name__ == '__main__':
    main(sys.argv)

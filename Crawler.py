import requests
import time
import json
import sys
from bs4 import BeautifulSoup


ptt_url = 'https://www.ptt.cc'



def checkStatus(url):
    
    response = requests.get(url = url, cookies = {'over18':'1'})

    if response.status_code != 200:
        return None
    else:
        return response.text

    pass

def get_articles(response_text,date):
    
    soup = BeautifulSoup(response_text,'html.parser')
    pre_div = soup.find('div','btn-group btn-group-paging')
    #Get previous page
    pre_url = pre_div.find_all('a')[1].get('href')

    articles = []
    divs = soup.find_all('div','r-ent')
    for d in divs:

        if d.find('div','date').text.strip() == date:
            
            pushCount = 0
            pushStr = d.find('div','nrec').text
            
            if pushStr:

                try:
                    pushCount = int(pushStr)
                
                except ValueError:
                    if pushStr == "爆":
                        pushCount = 99
                    
                    elif pushStr.startswith("X"):
                        pushCount = -10

            if d.find('a'):

                #href = d.find('a').href
                href = d.find('a').get('href')
                articleTitle = d.find('a').text
                author = ''
                articles.append({
                    'title':articleTitle,
                    'href':href,
                    'author':author,
                    'pushCount':pushCount
                })

    return articles,pre_url


# def Crawling(url_reponse):

#     if url_reponse:
#         articles = []
#         today = time.strftime("%m/%d").lstrip('0')

#     pass


def main(argv):
    print (get_articles(checkStatus(argv[1]),argv[2]))
    pass

if __name__ == '__main__':
    main(sys.argv)
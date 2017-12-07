import sys
import time
import json
import requests
from bs4 import BeautifulSoup

ptt_url = 'https://www.ptt.cc'

def check_status(url):
    """Check Url status"""
    response = requests.get(url=url, cookies={'over18':'1'})

    if response.status_code != 200:
        return None
    return response.text

def get_articles(response_text, date):
    """Get all articles information in the page, return JSON format"""
    soup = BeautifulSoup(response_text, 'html.parser')
    pre_div = soup.find('div', 'btn-group btn-group-paging')
    #Get previous page
    pre_url = pre_div.find_all('a')[1].get('href')
    articles = []
    div_set = soup.find_all('div', 'r-ent')

    for div in div_set:
        author = div.find('div', 'author').text

        if div.find('div', 'date').text.strip() == date:
            push_count = 0
            push_str = div.find('div', 'nrec').text

            if push_str:
                try:
                    push_count = int(push_str)
                    
                except ValueError:
                    if push_str == "爆":
                        push_count = 99
                    elif push_str.startswith("X"):
                        push_count = -10

            if div.find('a'):
                href = div.find('a').get('href')
                article_title = div.find('a').text
                articles.append({
                    "title":article_title,
                    "href":href,
                    "author":author,
                    "pushCount":push_count
                })

    return articles, pre_url

# def Crawling(url_reponse):

#     if url_reponse:
#         articles = []
#         today = time.strftime("%m/%d").lstrip('0')

#     pass

def main(argv):
    """Main Function"""
    print(get_articles(check_status(argv[1]), argv[2]))

if __name__ == '__main__':
    main(sys.argv)

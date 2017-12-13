import ArticleCrawler
import MongoConnect
import ImageCrawler
import pprint
import Logger

ptt_url = 'https://www.ptt.cc/bbs/'
target_board = ["Gossiping", "Sex", "Beauty", "Tech_Job"]
for board in target_board:
    url = ptt_url+board+'/index.html'
    article_set, article_len = Crawler.start(url, 30)
    Logger.log_info(__name__, '{0} complete.'.format(board))
    for article in article_set:
        try:
            MongoConnect.insert_mongo('ptt', board, article)
            Logger.log_info(__name__,'insert {0} articles to mongo - {1}.'.format(article_len, board))
        except Exception:
            Logger.log_exception(__name__, Exception)
        

import requests
import re
from bs4 import BeautifulSoup as bs
import json
import time
interval_time = 2

if __name__ == '__main__':

    for i in range(7399901, 7622375):
        url = "https://ask.csdn.net/questions/"+str(i)
        headers = []
        attempts = 0
        success = False
        while attempts < 100 and not success:
            try:
                res = requests.get(url, headers = headers)
                time.sleep(interval_time)
                success = True
            except:
                attempts += 1
                if attempts == 100:
                    print('get '+str(i)+' down')
                    break
        if not success:
            continue
        txt = res.text
        soup = bs(txt, 'lxml')
        
        
    '''
    for i in range(200):
        articles = []
        with open('csdn_data/article_links_'+str(i)+'.json', 'r') as f:
            article_links = json.load(f)
            for j,link in enumerate(article_links):
                try:
                    info = get_article_info(link)
                except:
                    continue
                articles.append(info)
                if j%10000 == 0:
                    print(str(j)+' is over')
            with open('articles_data/articles_'+str(i)+'.json', 'w') as f:
                json.dump(articles, f, ensure_ascii = False)
            print('finish ', i)
        print('------------------over----------------------')
    '''
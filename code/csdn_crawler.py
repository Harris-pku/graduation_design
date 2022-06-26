import requests
import re
from bs4 import BeautifulSoup as bs
import json
import time
interval_time = 2
def get_all_homepage():
    link_set = set()
    author_set = set()
    for i in range(200):
        url = "https://ask.csdn.net/"
        headers = {
            "accept": "text/plain, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }
        data = {
            "CategoryType": "SiteHome",
            "ParentCategoryId": 0,
            "CategoryId": 808,
            "PageIndex": i+1,
            "TotalPostCount": 4000,
            "ItemListActionName": "AggSitePostList",
        }
        attempts = 0
        success = False
        while attempts < 100 and not success:
            try:
                rp = requests.post(url, headers=headers, json=data)
                time.sleep(interval_time)
                success = True
            except:
                attempts += 1
                if attempts == 100:
                    print('get homepage fucked up')
                    break
        if not success:
            continue
        txt = rp.text
        soup = bs(txt,'lxml')
        post_items = soup.find_all("div",class_ = "post-item-text")
        post_foots = soup.find_all('footer',class_ = "post-item-foot")
        for post in post_items:
            link = post.find('a',class_ = 'post-item-title')['href']
            link_set.add(link)
        for foot in post_foots:
            author = foot.find('a',class_ = 'post-item-author')['href'][24:-1]
            author_set.add(author)
        #print("already get "+str(len(author_set))+' from homepage')
    return link_set,author_set        
        
def expand_users_by_followee(all_authors,authors):
    cookie = '__gads=ID=3de2898e56fd728c:T=1560001091:S=ALNI_MYlSeZ5qz2c33HihJTEOBOLu3qLVg; Hm_lvt_40bc57a179f7897af8f7978f96452f84=1585296459; sc_is_visitor_unique=rx12051111.1585296461.2288D063C6184F95C26B6DB56D143013.1.1.1.1.1.1.1.1.1-9356454.1577070165.1.1.1.1.1.1.1.1.1; UM_distinctid=17598b6c91f82b-051c6b0aa965a6-303464-144000-17598b6c92061e; _ga=GA1.1.1031539787.1560001092; .Cnblogs.AspNetCore.Cookies=CfDJ8AHUmC2ZwXVKl7whpe9_lasR0t89wJGKdQUOR9sQ8yVPMjuvMoYo0yBj-mwU7yafSMAAZYYmsQqSZsxKVBx_-jnhv9boYmzI1eQ5bWcUlVLYmICxOdJ3k1uqT0XGrxreQMVcUlEBAw4cJPebB_K-T3EhquB-YxHxaY3NIxkoeLRoW9U4xLwPRRkDJ19F0JEQwiK9aeGb2bL8qH9JrOsJn3cHrCLKDMlAA1r5pAx7ba8_1FoGCIIWIacrb4f1F7lzlSvEJKj-31Ke5T9Su8W2UXdQBIYMjxlI0N0DNmvhVU0LTZUc4qkXte1eynqzoq8qefCZ7QpcteNhdkgwiqfRQCowOzub5rK9Uy38A2303D-JDRblKGn_n3NZahGCm97_hKcTzicgz3HxmnCHrK-vUCynvXs_IyiP_tvko6PPzFXzahDqWJgRRAGfgShVgkQP08202aSaO8W3SJXmGV6bKB7jxNnhYlBqyJD5hPXVqql4YNgI6pDxgtuBe7mrM3Er7Wiabmt7NppojwJFkfNq1VxbZRZTzrITvBVqhDr8egwBfrFO4oPS0wfh_mJOpW0zLQ; .CNBlogsCookie=D52E41835197FCAA5B64E7C3E10E48CEF50AB68508819014427A6FDD633BAD0CC58D8A39F584E93289418CAEFEDEF6291D19EF206000E68CB14292F2920FCB19DE9E357AB666A920099240643747644AEC601201; _ga_4CQQXWHK3C=GS1.1.1605794806.2.1.1605795365.0'
    followees = set()
    solved_authors = []
    for author in authors:
        #print('getting '+author+'\'s followee' )
        url = "https://home.cnblogs.com/u/"+author+"/followees/"
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'cache-control': 'max-age=0',
            'cookie':cookie,
            'referer': 'https://www.cnblogs.com/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
        }
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
                    print('get followee fucked up '+url)
                    break
        if not success:
            continue
        txt = res.text
        soup = bs(txt,'lxml')
        if res.status_code == 404 or res.status_code == 204:
            solved_authors.append(author)
            continue
        try:
            followee_num = int(soup.find('a',class_ = 'current_nav').text.split('(')[1].split(')')[0])
        except:
            print(url)
            exit()
        if followee_num == 0:
            solved_authors.append(author)
            continue
        page_num = (followee_num-1)//45+1
        for page in range(page_num):
            url = "https://home.cnblogs.com/u/"+author+"/followees/?page="+str(page+1)
            attempts = 0
            success = False
            while attempts < 100 and not success:
                try:
                    res = requests.get(url,headers = headers)
                    time.sleep(interval_time)
                    success = True
                except:
                    attempts += 1
                    if attempts == 100:
                        print('get followee fucked up '+url)
                        break
            if not success:
                continue
            txt = res.text
            soup = bs(txt,'lxml')
            avatar_list = soup.find('div',class_='avatar_list')
            if avatar_list is None:
                print(url)
                exit()
            avatar_list = avatar_list.ul
            lis = avatar_list.find_all('li')
            for li in lis:
                followee = li.a['href'][3:]
                if followee not in all_authors:
                    followees.add(followee)
                    if len(followees)%1000==0:
                        with open('cnblogs_data/add_authors.json','r') as f:
                            old_authors = set(json.load(f))
                        new_authors = old_authors|followees
                        with open('cnblogs_data/add_authors.json','w') as f:
                            json.dump(list(new_authors),f)
                        print('get another 1000 new authors')
                #print('followee is '+followee)
        solved_authors.append(author)
        if len(solved_authors)>1000:
            with open('cnblogs_data/authors.json','r') as f:
                old_solved_authors = json.load(f)
            with open('cnblogs_data/authors.json','w') as f:
                json.dump(list(set(old_solved_authors+solved_authors)),f)
            with open('cnblogs_data/add_authors.json','r') as f:
                old_added_authors = json.load(f)
            with open('cnblogs_data/add_authors.json','w') as f:
                json.dump(list(set(old_added_authors)-set(solved_authors)),f)
            solved_authors = []
            print('done with another 1000 authors')
    with open('cnblogs_data/authors.json','r') as f:
        old_solved_authors = json.load(f)
    with open('cnblogs_data/authors.json','w') as f:
        json.dump(list(set(old_solved_authors+solved_authors)),f)
    with open('cnblogs_data/add_authors.json','r') as f:
        old_added_authors = set(json.load(f))
    with open('cnblogs_data/add_authors.json','w') as f:
        old_added_authors = old_added_authors-set(solved_authors)
        old_added_authors = old_added_authors|followees
        json.dump(list(old_added_authors),f)
    return followees

def get_article_by_user(user):
    article_link_list = []
    for i in range(1, 10000):
        url = "http://www.cnblogs.com/%s/default.html?page=%d" % (user, i)
        attempts = 0
        success = False
        while attempts < 100 and not success:
            try:
                res = requests.get(url)
                if res.status_code != 500:
                    success = True
            except:
                attempts += 1
                if attempts == 100:
                    print('get article fucked up '+url)
                    break
        if not success:
            print('not success')
            raise Exception(print(url))
        if res.status_code == 404 or res.status_code == 204:
            return article_link_list
        elif res.status_code!=200:
            print('status code:',res.status_code)
            raise Exception(print(url))
        txt = res.text
        soup = bs(txt,'lxml')
        all_article_link = soup.find_all('a',class_ = 'postTitle2 vertical-middle')
        if len(all_article_link)==0:
            break
        for article_link in all_article_link:
            link = article_link['href']
            article_link_list.append(link)
    return article_link_list

def get_article_info(url):
    cookie = '__gads=ID=3de2898e56fd728c:T=1560001091:S=ALNI_MYlSeZ5qz2c33HihJTEOBOLu3qLVg; _dx_uzZo5y=5a6b8e0400ff78c122d26d8c2be42e5f46bf7b5e29538598d6d2f58276837ad359dcad00; Hm_lvt_40bc57a179f7897af8f7978f96452f84=1585296459; sc_is_visitor_unique=rx12051111.1585296461.2288D063C6184F95C26B6DB56D143013.1.1.1.1.1.1.1.1.1-9356454.1577070165.1.1.1.1.1.1.1.1.1; Hm_lvt_95eb98507622b340bc1da73ed59cfe34=1587307560; CNZZDATA1275508084=1916855719-1596348684-null%7C1596348684; CNZZDATA1258637387=773414821-1602420857-https%253A%252F%252Fwww.baidu.com%252F%7C1602420857; CNZZDATA1261691463=192988720-1603959772-https%253A%252F%252Fwww.baidu.com%252F%7C1603959772; UM_distinctid=17598b6c91f82b-051c6b0aa965a6-303464-144000-17598b6c92061e; CNZZDATA1254128672=271671658-1604580383-https%253A%252F%252Fwww.google.com%252F%7C1604580383; CNZZDATA1278590822=1363603512-1604586510-https%253A%252F%252Fwww.cnblogs.com%252F%7C1604586510; _ga=GA1.1.1031539787.1560001092; .Cnblogs.AspNetCore.Cookies=CfDJ8AHUmC2ZwXVKl7whpe9_lasR0t89wJGKdQUOR9sQ8yVPMjuvMoYo0yBj-mwU7yafSMAAZYYmsQqSZsxKVBx_-jnhv9boYmzI1eQ5bWcUlVLYmICxOdJ3k1uqT0XGrxreQMVcUlEBAw4cJPebB_K-T3EhquB-YxHxaY3NIxkoeLRoW9U4xLwPRRkDJ19F0JEQwiK9aeGb2bL8qH9JrOsJn3cHrCLKDMlAA1r5pAx7ba8_1FoGCIIWIacrb4f1F7lzlSvEJKj-31Ke5T9Su8W2UXdQBIYMjxlI0N0DNmvhVU0LTZUc4qkXte1eynqzoq8qefCZ7QpcteNhdkgwiqfRQCowOzub5rK9Uy38A2303D-JDRblKGn_n3NZahGCm97_hKcTzicgz3HxmnCHrK-vUCynvXs_IyiP_tvko6PPzFXzahDqWJgRRAGfgShVgkQP08202aSaO8W3SJXmGV6bKB7jxNnhYlBqyJD5hPXVqql4YNgI6pDxgtuBe7mrM3Er7Wiabmt7NppojwJFkfNq1VxbZRZTzrITvBVqhDr8egwBfrFO4oPS0wfh_mJOpW0zLQ; .CNBlogsCookie=D52E41835197FCAA5B64E7C3E10E48CEF50AB68508819014427A6FDD633BAD0CC58D8A39F584E93289418CAEFEDEF6291D19EF206000E68CB14292F2920FCB19DE9E357AB666A920099240643747644AEC601201; _ga_4CQQXWHK3C=GS1.1.1605794806.2.1.1605795365.0; CNZZDATA1278852858=74305386-1606045283-%7C1606045283'
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'cache-control': 'max-age=0',
            'cookie':cookie,
            'referer': 'https://www.cnblogs.com/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
        }
    attempts = 0
    success = False
    while attempts < 100 and not success:
        try:
            res = requests.get(url)
            if res.status_code != 500:
                success = True
        except:
            attempts += 1
            if attempts == 100:
                print('get article fucked up '+url)
                break
    if not success:
        #print('ok')
        print('not success')
        raise Exception(print(url))
    if res.status_code == 404 or res.status_code == 204:
        return dict()
    elif res.status_code != 200:
        #print(res.status_code)
        print('status code:',res.status_code)
        raise Exception(print(url))
    txt = res.text
    soup = bs(txt,'lxml')
    ret = dict()
    ret['url'] = url
    ret['title'] = list(soup.find('a',class_ = 'postTitle2 vertical-middle').stripped_strings)[0]
    ret['texts'] = list(soup.find('div',class_ = 'blogpost-body').stripped_strings)
    raw_codes = soup.findAll('div',class_ = 'cnblogs_code')
    codes = []
    for code in raw_codes:
        codes.append(code.get_text())
    ret['codes'] = codes
    blogID = re.findall('cb_blogId = [1234567890]*',res.text)[0].split('cb_blogId = ')[1]
    postID = url.split('/')[-1].split('.')[0]
    new_url = url.split('/p')[0]+'/ajax/CategoriesTags.aspx?blogId='+blogID+'&postId='+postID
    res = requests.get(new_url)
    soup = bs(res.text,'lxml')
    raw_tag = soup.find('div',id = 'EntryTag')
    if raw_tag is None:
        tag = None
    else:
        tag = list(raw_tag.stripped_strings)[1::2]
    raw_cate = soup.find('div',id = 'BlogPostCategory')
    if raw_cate is None:
        category = None
    else:
        category = list(raw_cate.stripped_strings)[1::2]
    ret['tags'] = tag
    ret['categorys'] = category
    return ret
    
    
if __name__ == "__main__":
    
    for i in range(43,112):
        articles = []
        with open('cnblogs_data/article_links_'+str(i)+'.json','r') as f:
            article_links = json.load(f)
        for j,link in enumerate(article_links):
            try:
                info = get_article_info(link)
            except:
                continue
            articles.append(info)
            if j%10000==0:
                print(str(j)+' is over')
        with open('articles_data/articles_'+str(i)+'.json','w') as f:
            json.dump(articles,f,ensure_ascii = False )
        print('finish ', i)
    print('------------------over--------------------------')
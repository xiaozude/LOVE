import urllib.request
import re
import os

user_agent = {'User-Agent' :
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko) ' +
        'Chrome/79.0.3945.130 Safari/537.36'}

def get_data(url, data = None, head = user_agent):
    request = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

def get_image():
    url_re = r'http://h1.ioliu.cn/bing/.*?_1920x1080.jpg'
    host = 'https://bing.ioliu.cn/?p='
    
    url = set()
    name = 1
    for page in range(1, 120):
        print('page', page)
        html = get_data(host+str(page)).decode('utf-8')
        index = 0
        while True:
            s = re.search(url_re, html[index:])
            if s == None:
                break
            i,j = s.span()
            if s.group() not in url: 
                url.add(s.group())
                with open(str(name) +'.jpg', 'wb') as file:
                    file.write(get_data(s.group()))
                print('\timage', name)
                name += 1
            index += j
    return None

os.chdir('image')
get_image()
os.chdir('..')

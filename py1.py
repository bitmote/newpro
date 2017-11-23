#!/usr/bin/env python
# coding=utf-8
#http://www.newsmth.net/nForum/#!article/Fish/93370
#给定上述网址，对该帖进行回帖
#首先取出id号,然后取出标题对标题进行url编码
import requests
import re
from bs4 import BeautifulSoup
from urllib import quote,quote_plus
#response = requests.get('http://www.newsmth.net/nForum/article/Fish/93370?ajax')
url = 'http://www.newsmth.net/nForum/#!article/Fish/93370'
ajaxurl  = url.replace('#!','')+'?ajax'
print url
ajaxcontent = requests.get(ajaxurl)
soup = BeautifulSoup(ajaxcontent.text,'html.parser')
content = soup.find('title').get_text()
print content
print quote((content).encode('utf-8'))
print re.sub(r'\d+',"ajax",url)
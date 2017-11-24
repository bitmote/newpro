#coding=utf8
import requests
import time
import re
from bs4 import BeautifulSoup
#http://www.newsmth.net/nForum/#!article/Fish/93370
#给定上述网址，对该帖进行回帖
#首先取出id号,然后取出标题,对标题进行url编码,然后就可以对内容进行编辑然后回帖了
#取ID号
#一个规范的地址，就是取最后的几位阿拉伯数字,可采用正则表达式
from urllib import quote
smthurl = 'http://www.newsmth.net/nForum/#!article/Fish/93304'
res = re.findall(r'(\d+)',smthurl)
id= res[0]

headers = {
    'Host':'www.newsmth.net',
    'Origin':'http://www.newsmth.net',
    'Referer':'http://www.newsmth.net/nForum/',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

url = 'http://www.newsmth.net/nForum/user/ajax_login.json'
session = requests.session()
session.get('http://www.newsmth.net')
payload = {'id':'yyhn1959','passwd':'yourpw'}
time.sleep(2)
con = session.post(url,data = payload,headers = headers)
print con.status_code
#取出标题并编码   因为是ajax异步加载，所以在该网址的源代码里是没有标题信息的，需要获取真正的地址就是  http://www.newsmth.net/nForum/#!article/Fish/93370  去掉#!  加上?ajax
ajaxurl = smthurl.replace('#!','')+'?ajax'
ajaxcontent = session.get(ajaxurl)
soup = BeautifulSoup(ajaxcontent.text,'html.parser')
unititle = 'Re: '+soup.find('title').get_text()
title = unititle.encode('utf-8')
#进行url编码
urltitle = quote(title)
content = 'got it'
postcontent = {'content':content,'id':id,'subject':urltitle}
#http://www.newsmth.net/nForum/article/Fish/ajax_post.json
#计算posturl  使用这则表达式
ajaxurl = re.sub(r'\d+','ajax_post.json',smthurl.replace('#!',''))
session.post(ajaxurl,data = postcontent, headers = headers)


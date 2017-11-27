#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
#获取水木论坛军事版面的图片，首先，给的版面的网址，需要进一步去获取版面的帖子地址
#在获取帖子地址后，需要进行图片的获取
#用到了BeautifulSoup

url = 'http://www.newsmth.net/nForum/#!board/Picture'
ajaxurl = 'http://www.newsmth.net/nForum/board/Picture?ajax&p=2'
page = requests.get(ajaxurl)
soup = BeautifulSoup(page.content,'html.parser')

#使用BeautifulSoup提取网页地址
#地址形式如下  <td class='title-9'> <a href=url>

#找到网址，继续找出网址中的图片地址
def geturl(picurl):
    page = requests.get(picurl)
    picsoup = BeautifulSoup(page.content,'html.parser')
    #print picsoup.prettify()
    piclist = picsoup.find_all('img',src=re.compile(r'//att.newsmth.net/nForum/'))
    #找到每张图片的详细地址，并在本地下载
    local = '/Users/mavisluo/Desktop/folder/picfiles/'
    for pic in piclist:
        img = 'http://' + pic['src'][2:]
        wordlist = re.split(r'/',img)
        filename = wordlist[-3]+wordlist[-2]+'.jpeg'
        picfile = requests.get(img)
        imgfile = local + filename
        with(open(imgfile,'wb')) as f:
            f.write(picfile.content)
            f.close()

milurl = soup.find_all('td',attrs = {'class':'title_9',})
schema = 'http://www.newsmth.net'
for td in milurl:
    geturl(schema + td.a['href'])










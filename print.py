#encoding:UTF-8
from bs4 import BeautifulSoup
import requests
url = 'http://www.jianshu.com/trending/weekly?utm_medium=index-banner-s&utm_source=desktop'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
tag = soup.find_all('a',attrs = {'class':'title','target':'_blank'})
'''for item in tag:
    print item.get_text()

for people in name:
    print people.get_text()
    '''
name = soup.find_all('a',class_='nickname')
for people,item in zip(name,tag):
    print people.get_text(),'    ',item.get_text()
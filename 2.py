#====youtube爬虫频道. 添加翻页.


import requests



params = {"scroll": "true", "page": 10}


jieguo1=requests.get('https://www.youtube.com/@laogao/videos',params=params)
# print(jieguo1.text)

from bs4 import BeautifulSoup

a=jieguo1.text
soup = BeautifulSoup(a, 'html.parser')
# print(soup.prettify())



with open('tmp.html','w',encoding='utf-8') as f:
   f.write(a)


from lxml import etree
save={}
jibenxinxi=[]

aa=etree.HTML(a)
print(1)
tmp=aa.xpath('//div[@id="details"]')
tmp=aa.xpath('//div')



# 阿里大模型计费:

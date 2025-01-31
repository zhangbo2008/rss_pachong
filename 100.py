# 2025-01-31,13点14 爬虫
'''
https://www.biccamera.com/bc/category/001/100/150/125/005/?sort=01
https://www.amazon.co.jp/dp/B0DTSN2K86?th=1&psc=1&m=AN1VRQENFRJN5&tag=twm1abf-22&linkCode=ogi
https://www.amazon.co.jp/dp/B0DV9BSDSM?th=1&psc=1&m=AN1VRQENFRJN5&tag=twm1abf-22&linkCode=ogi
https://www.amazon.co.jp/dp/B0DS2Z8854?th=1&psc=1&m=AN1VRQENFRJN5&tag=twm1abf-22&linkCode=ogi
https://www.amazon.co.jp/dp/B0DT7GMXHB?th=1&psc=1&m=AN1VRQENFRJN5&tag=twm1abf-22&linkCode=ogi
https://www.amazon.co.jp/dp/B0DT6Q3BXM?th=1&psc=1&m=AN1VRQENFRJN5&tag=twm1abf-22&linkCode=ogi


'''



url='https://www.amazon.co.jp/dp/B0DTSN2K86?th=1&psc=1&m=AN1VRQENFRJN5&tag=twm1abf-22&linkCode=ogi'


from bs4 import BeautifulSoup 



# import requests
# # a=requests.get(url)
# a=requests.get('https://www.amazon.co.jp/dp/B0DTSN2K86?th=1&psc=1&m=AN1VRQENFRJN5&tag=twm1abf-22&linkCode=ogi').text
# soup = BeautifulSoup(a, 'lxml')
# print(a)






# 爬虫技巧:https://www.zenrows.com/blog/selenium-python-web-scraping#save-resources
# https://www.zenrows.com/blog/selenium-slow#choose-selectors-with-better-performance
# 谷歌人机验证解决方法: https://blog.csdn.net/weixin_42096901/article/details/100593069






import re

import os
import io
import json
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # 解决跨域问题

import requests
from bs4 import BeautifulSoup



# ‌FORM=PERE1‌：搜索结果以卡片形式展示，适用于图片或视频等多媒体类搜索场景‌
# PC=U316‌：表示搜索是在个人电脑上进行的‌

from selenium import webdriver
import json
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


from selenium import webdriver
options = webdriver.ChromeOptions()

from selenium import webdriver
options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-gpu')  # 禁用GPU加速
options.add_argument('--headless')
options.add_argument("--blink-settings=imagesEnabled=false")
# 初始化 WebDriver

# 打开网页

#数据库保存用户信息.json 保存.     用户名--->data

''' # 密码保存md5加密后的.
#  zhangsan--->{
    "用户名":"zhangsan"
    "密码md5":"234kjcx79#xcilz"
    "订阅的频道":[
                  "youtube 中国人",
                  "youtube 看天下",
                  "bilibili 看狗",
    ],
    "收藏夹":[ 收藏文件的索引(2,3)                     
          ]
    }
    
    所有人的收藏夹---->[
       收藏1,
       收藏2
       收藏3...
    ]
'''
shoucang=[]
data_base={
  "zhangsan":{
    "用户名":"zhangsan",
    "密码md5":"111",
    "订阅的频道":[
                  "youtube 中国人",
                  "youtube 看天下",
                  "bilibili 看狗",
    ],
    "收藏夹":[ 2,3                 
          ]
    },
    "已阅读":set(
      ['aaa','bbb']
    )
  

  
}



import requests








import time
aaaaa=time.time()

if 1:
    print('开始爬虫.')
    url='https://www.amazon.co.jp/gp/product/B0BSLJ52ZF?&linkCode=sl1&tag=twm1a4080-22&linkId=387fac7c4d0581478539f94f3afea1ff&language=ja_JP&ref_=as_li_ss_tl'
    # url='https://www.baidu.com'
#     cookie='session-id=358-1808349-2151563; session-id-time=2082787201l; i18n-prefs=JPY; skin=noskin; ubid-acbjp=356-2093933-0778857; lc-acbjp=zh_CN; session-token="VNXhjIlj3QO9MDcQQBTqCExCdVOgyLGUACAFc6mI9VX6XBOl1bLrjQ5nY58BEleQL0+AqKk9kWnUaTPSUKxHBkre7kTQUz9BR4PIuzCnoSSUwy7pni3dU/j9+m6WzMuRHjIrT99CUYIYP5V6zXHfSUysyOBXUmnCCs34C8kOUiPDDbSs0EAT0aLycJQ0UPCL3dtWGSsREFrpkc+E4KE1UwIalMCpo4Q2HwnD2334++7GWvGZyGRlG0XO35KpR0LAO/75V1WKSlwjaraEyingpkKGmXXSkJKhzeV9cm8tLyd/awEdH4zXQiIIE8C4vLsufYHvmoTuDxhI1mtGIbTk2nNDKlvHn/mEcRVq+tgIjFg="
# '



    from webdriver_manager.chrome import ChromeDriverManager

    # driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver = webdriver.Chrome(options=options)
    
    
    driver.get(url)
    # driver.get('https://www.amazon.com/')
    
    data='csm-sid=990-8824169-1528533; x-amz-captcha-1=1738307795238584; x-amz-captcha-2=OCRw5f+2D+Go8vQObCoS1A==; session-id=358-1808349-2151563; session-id-time=2082787201l; i18n-prefs=JPY; skin=noskin; ubid-acbjp=356-2093933-0778857; lc-acbjp=zh_CN; session-token="q+h6n7X/jTtYWbUeZa1+Qs+eJfsX/C7pR+Y4um9cq3WAqYpJhuEBJgQebnJNV42yOLrP/721YDdvyQZVNOUiHWy15O/s+ttO/UUWKXSx4DAWkipRbKDAYU4cIy85Rklxlo/lkLCF6CA4CeABCItnYAKyHxyX1dQ9gS+Fuk4AO3Ak8d6rX+ZYF9VY/Bb1EAQu7DPwqYWV8SDlKCzMa51QFnCBf7ytoqh4aO+1WbHw/U9bm0zeXMa76XMn1FjOiLnelOnlmPSQo5kEiF9Mycz+Th7b0MnkjTA57ZaItT4DAMRtaOrqaJ6vguLcWtzV/0lodliCTqbreyTj9u2f7I41LrVjPH6+9juqLiX50MF/JvE="; csm-hit=tb:s-WH1GA60S58JBA1DSZPMS|1738331417475&t:1738331417475&adb:adblk_no'
    #解析data
    data=data.split(';')

    for i in data:
      print(i)
      driver.add_cookie({
    'name': i.split('=')[0].strip(),
    'value':i.split('=')[1].strip(),
  # 'domain': 'amazon.co.jp',
  # 'path': '/',
  #   'expiry': None  # 可以设置过期时间
})

    import time
    # driver.get('https://www.amazon.co.jp')
    driver.get(url)
    # time.sleep(150) # 查看效果
    if 1: 
      with open('debug.html' , 'w',encoding='utf-8') as f:
        f.write(driver.page_source)
    # driver.close()
    # a=driver.find_element(By.XPATH,'//div[@class="a-section a-spacing-none a-padding-none"]').text
    a=driver.find_element(By.XPATH,'//div[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]').text
    print("结果是",a)
    print('使用时间',time.time()-aaaaa)
    
    raise
    # print(driver.page_source)
    a=[i for i in driver.find_elements(By.XPATH,'//*[@jsname="UWckNb"]')]
    
    def guolv (a):
       print('过滤之前的名字',a)
       if 'https://www.youtube.com/@' in a:
        a=a.replace('https://www.youtube.com/@','')
        if '/' in a:
          a=a[:a.index('/')]
        if '?' in a:
          a=a[:a.index('?')]
          pass
        if '%' in a:
          return ''
        return a
       else:
         return ''
    out=[]
    for i in a:
       #=====每一个元素解析
       yuansu={}
       yuansu['name']=i.find_element(By.XPATH, './/*[@class="LC20lb MBeuO DKV0Md"]').text
       yuansu['uid']=guolv(i.get_attribute("href"))
       try:
         yuansu['pic']=i.find_element(By.XPATH,'../../../../..//img').get_attribute('src')
       except:
         yuansu['pic']=''
       out.append(yuansu)
       pass








    
    
    
    
    
    
    
    
    
    


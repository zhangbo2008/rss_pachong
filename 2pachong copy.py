#   pip install flask[async]
# 当pyppeteer下载Chromium失败时运行此脚本，找出浏览器应该存储的位置，手动下载该浏览器放到相应的路径下即可，下载地址：https://registry.npmmirror.com/binary.html?path=chromium-browser-snapshots/#/

# 下载地址: https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win_x64/
 # 先配置chrome
 
 # https://miyakogi.github.io/pyppeteer/index.html  说明书!!!!!!
 
 
 
 # # ValueError: signal only works in main thread of the main interpreter  https://blog.csdn.net/weixin_41822224/article/details/103719863
import pyppeteer.chromium_downloader
print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))
#!!!!!!!!!我下载的是: https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win_x64/1181217/    然后复制到  C:\Users\admin\AppData\Local\pyppeteer\pyppeteer\local-chromium\1181205\chrome-win\ 即可.





import pyppeteer

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
# async def main3():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('http://quotes.toscrape.com/js/')
#     doc = pq(await page.content())
#     print('Quotes:', doc('.quote').length)
#     await browser.close()
 
# asyncio.get_event_loop().run_until_complete(main3())









# 爬虫技巧:https://www.zenrows.com/blog/selenium-python-web-scraping#save-resources
# https://www.zenrows.com/blog/selenium-slow#choose-selectors-with-better-performance
# 谷歌人机验证解决方法: https://blog.csdn.net/weixin_42096901/article/details/100593069



import os
import io
import json
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # 解决跨域问题

import requests
if 0: # =========不用selenium了.
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
    driver = webdriver.Chrome(options=options)
 
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










@app.route('/login', methods=['GET', 'POST'])
def editorDatafd():
    r=request.json
    if r['name'] in data_base:
      return jsonify(data_base[r['name']])
    return jsonify('请先注册')


















@app.route('/huoqu_bilibili_channels', methods=['GET', 'POST'])
def editorData3433333():
    r=request.json
    # r['name']='中国'
    q=r['name']

    import time
    aaa=time.time()
    url=f"https://search.bilibili.com/upuser?keyword={q}"
    # a1=requests.get(url)
    driver.get(url)
    print("get网页的用时",time.time()-aaa)
    a_1=[i for i in driver.find_elements(By.XPATH,'//a[@class="text1 p_relative"]')]
    # print(a)

    a=[i.get_attribute('title') for i in a_1]
    a_uid=[i.get_attribute('href') for i in a_1]
    a_uid=[i[i.index('.com/')+5:] for i in a_uid]
    # print(a)
    import re 
    def guolv (a):
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
    # a=[guolv(i) for i in a ]
    out=[(i,j) for i,j in zip(a,a_uid)]
    # print('过滤之后的',a)
    # print(a)
    # a=[i.text for i in driver.find_elements(By.XPATH,'//div[@class="yuRUbf"]')]
    # print(a)
    print('解析结果的用时',time.time()-aaa)
    # driver.save_screenshot("screenshot_with-no-image.png")
    return jsonify(out)






#========youtube, X 都进行了防爬虫. 所以我们只能用谷歌site来搜.
if 0:# test:

    q='china'

    import time
    aaa=time.time()
    url=f"https://x.com/search?q={q}&src=typed_query&f=user"
    url=f"https://www.youtube.com/results?search_query={q}&sp=EgIQAg%253D%253D"
    url=f"https://www.google.com/search?q=site%3Ahttps%3A%2F%2Fx.com%2F%40+{q}"
    # a1=requests.get(url)
    driver.get(url)
    print(driver.page_source)
    a=[i for i in driver.find_elements(By.XPATH,'//*[@jsname="UWckNb"]')]
    print(a)
    a=[i.get_attribute('href') for i in a]
    print(a)
    import re 
    def guolv (a):
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
    a=[guolv(i) for i in a ]
    a=[i for i in a if i]
    b=[]
    for i in a:
      if i not in b:
         b.append(i)
    a=b
    print('过滤之后的',a)
    print(a)
    # a=[i.text for i in driver.find_elements(By.XPATH,'//div[@class="yuRUbf"]')]
    # print(a)
    print(time.time()-aaa)
    











# demo:  https://rsshub.app/twitter/user/zlj517
@app.route('/huoqu_X_channels', methods=['GET', 'POST'])
def editorData33232433333():
    r=request.json
    # r['name']='中国'
    q=r['name']

    # q='china'

    import time
    aaa=time.time()
    url=f"https://x.com/search?q={q}&src=typed_query&f=user"
    url=f"https://www.youtube.com/results?search_query={q}&sp=EgIQAg%253D%253D"
    url=f"https://www.google.com/search?q=site%3Ax.com%2F+{q}"
    # a1=requests.get(url)
    driver.get(url)
    print(driver.page_source)
    a=[i for i in driver.find_elements(By.XPATH,'//*[@jsname="UWckNb"]')]
    a_name=[i.text for i in driver.find_elements(By.XPATH,'//*[@class="LC20lb MBeuO DKV0Md"]')]
    print(a)
    a=[i.get_attribute('href') for i in a]
    print(a)
    import re 
    def guolv (a):
       if 'https://x.com/' in a:
        a=a.replace('https://x.com/','')
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
    a=[guolv(i) for i in a ]
    out=[(i,j) for i,j in zip(a,a_name)]

    print(time.time()-aaa)
    return jsonify(out)


# demo:  https://rsshub.app/twitter/user/zlj517
@app.route('/huoqu_youtube_channels3333333333', methods=['GET', 'POST'])
def editorData332324332423333333333333333333333333333333333():
    r=request.json
    # r['name']='中国'
    q=r['name']

    # q='china'

    import time
    aaa=time.time()

    url=f"https://www.google.mn/search?q=site%3Ayoutube.com/@%2F+{q}"
    # a1=requests.get(url)
    driver.get(url)
    time.sleep(1)
    if 1: 
      with open('debug.html' , 'w',encoding='utf-8') as f:
        f.write(driver.page_source)
    # print(driver.page_source)
    a=[i for i in driver.find_elements(By.XPATH,'//*[@jsname="UWckNb"]')]
    a_name=[i.text for i in driver.find_elements(By.XPATH,'//*[@class="LC20lb MBeuO DKV0Md"]')]
    a_pic=[i.get_attribute('src') for i in driver.find_elements(By.XPATH,'//div[@class="uhHOwf ez24Df"]/img')]
    print("图片地址",a_pic)
    # a_cite=[i.text for i in driver.find_elements(By.XPATH,'//div[@class="byrV5b"]/cite')]
    # print(a_cite,999999999999999999999)
    a=[i.get_attribute('href') for i in a]
    # print(a)
    import re 
    def guolv (a):
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
    a=[guolv(i) for i in a ]
    out=[(j,i,k) for i,j,k in zip(a,a_name,a_pic)]

    print(time.time()-aaa)
    return jsonify(out)

# import nest_asyncio
# nest_asyncio.apply()


import asyncio	
# demo:  https://rsshub.app/twitter/user/zlj517





# ValueError: signal only works in main thread of the main interpreter
@app.route('/huoqu_youtube_channels', methods=['GET', 'POST'])
async def xxx():  # 每一个服务都另起一个browser. 这样快.
    r=request.json
    q=r['name']

    from pyppeteer import launch
    browser = await launch({'handleSIGINT':False,
'handleSIGTERM': False,
'handleSIGHUP': False,})
    page = await browser.newPage()
    url=f"https://www.google.mn/search?q=site%3Ayoutube.com/@%2F+{q}"
    await page.goto(url)
    a=await page.xpath('//*[@jsname="UWckNb"]')
    print(a)
    def guolv (a):
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
       element =await i.xpath( '//*[@class="LC20lb MBeuO DKV0Md"]')
       print('element ', element)
       yuansu['name'] = await page.evaluate('(element) => element.textContent', element[0])

       yuansu['uid'] =guolv( await page.evaluate(
                '(i) => i.href',
                i
        ))
       try:
         yuansu['pic']=i.xpath('../../../../..//img').get_attribute('src')
       except:
         yuansu['pic']=''
       out.append(yuansu)
       pass
    print(out)
    return jsonify('1')





# ValueError: signal only works in main thread of the main interpreter
@app.route('/huoqu_youtube_channels2', methods=['GET', 'POST'])
async def xx33333333x():  # 每一个服务都另起一个browser. 这样快.
    r=request.json
    q=r['name']

    from pyppeteer import launch
    browser = await launch({'handleSIGINT':False,
'handleSIGTERM': False,
'handleSIGHUP': False,
"headless":True})
    page = await browser.newPage()
    
    
    
    url=f"https://www.google.mn/search?q=site%3Ayoutube.com/@%2F+{q}"
# a1=requests.get(url)
    # driver.get(url)
    await page.goto(url)
    await page.screenshot()
    a=await page.xpath('//div[@class="g Ww4FFb vt6azd tF2Cxc asEBEc"]')
    # b=await page.xpath('//img')
# //*[@jsname="UWckNb"]
    # print(a,"父节点!!!!!!!!!!")
    # print(b,"图片节点!!!!!!!!!!")
    content = await page.evaluate('document.body.textContent', force_expr=True)
    with open("aaa.txt",'w',encoding='utf-8') as f:
        f.write(content)
    print('html',content)
    
    def guolv (a):
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
    await page.waitForSelector('.uhHOwf ez24Df', { 'visible': True })
    for i in a:
       #=====每一个元素解析
       yuansu={}
       element =await i.xpath( './/*[@jsname="UWckNb"]/h3')
       yuansu['name'] = await page.evaluate('(element) => element.textContent', element[0])
       
       
       
       element2 =await i.xpath( './/*[@jsname="UWckNb"]')
       yuansu['uid'] = await page.evaluate('(element2) => element2.href', element2[0])
       
       


       try:
         print(1)
        #  e=await i.xpath('.//div[@class=""uhHOwf ez24Df""]')
         e=await i.xpath('.//img')
         print('图片',e)
         yuansu['pic']= await page.evaluate(
                '(e) => e.src',
                e[0]
        )
       except:
         yuansu['pic']=''
       out.append(yuansu)
       pass
    
    
    
    
    
    
    # print(out)
    # raise
    # print(out)
    
    return jsonify(out)

@app.route('/huoqu_youtube_channels555555555', methods=['GET', 'POST'])
async def editorData332324332423333():
    # result = await xxx()
    # return result
    # return jsonify(asyncio.get_event_loop().run_until_complete(main3()))
    # r['name']='中国'
    r=requests.json
    q=r['name']

    # q='china'

    import time
    aaa=time.time()

    url=f"https://www.google.mn/search?q=site%3Ayoutube.com/@%2F+{q}"
    # a1=requests.get(url)
    driver.get(url)
    time.sleep(1)
    if 0: 
      with open('debug.html' , 'w',encoding='utf-8') as f:
        f.write(driver.page_source)
    # print(driver.page_source)
    a=[i for i in driver.find_elements(By.XPATH,'//*[@jsname="UWckNb"]')]
    
    def guolv (a):
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
       yuansu['name']=i.find_element(By.XPATH, '//*[@class="LC20lb MBeuO DKV0Md"]').text
       yuansu['uid']=guolv(i.get_attribute("href"))
       try:
         yuansu['pic']=i.find_element(By.XPATH,'../../../../..//img').get_attribute('src')
       except:
         yuansu['pic']=''
       out.append(yuansu)
       pass
    
    
    
    
    
    
    
    # a_name=[i.text for i in driver.find_elements(By.XPATH,'//*[@class="LC20lb MBeuO DKV0Md"]')]
    # a_pic=[i.get_attribute('src') for i in driver.find_elements(By.XPATH,'//div[@class="uhHOwf ez24Df"]/img')]
    # print("图片地址",a_pic)
    # # a_cite=[i.text for i in driver.find_elements(By.XPATH,'//div[@class="byrV5b"]/cite')]
    # # print(a_cite,999999999999999999999)
    # a=[i.get_attribute('href') for i in a]
    # # print(a)
    # import re 

    # a=[guolv(i) for i in a ]
    # out=[(j,i,k) for i,j,k in zip(a,a_name,a_pic)]

    # print(time.time()-aaa)
    return jsonify(out)









if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    



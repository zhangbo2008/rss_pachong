# 爬虫技巧:https://www.zenrows.com/blog/selenium-python-web-scraping#save-resources
# https://www.zenrows.com/blog/selenium-slow#choose-selectors-with-better-performance
# 谷歌人机验证解决方法: https://blog.csdn.net/weixin_42096901/article/details/100593069

gugelis=[
"蒙古 google.mn蒙古语",
"韩国 google.co.kr 韩语",
"日本 google.co.jp 日语",
"越南 google.com.vn 越南语",
"老挝 google.la 老挝语",
"柬埔寨 google.com.kh 高棉语",
"泰国 google.co.th 泰语",
"马来西亚 google.com.my 马来语",
"新加坡 google.com.sg 马来语",
"文莱达鲁萨兰国 google.com.bn 马来语",
"菲律宾 google.com.ph 菲律宾语",
"印度尼西亚 google.co.id 印尼语",
"东帝汶 google.tp 葡萄牙语",
"哈萨克斯坦 google.kz 哈萨克语",
"吉尔吉斯斯坦 google.kg 吉尔吉斯语",
"塔吉克斯坦 google.com.tj 塔吉克语",
"乌兹别克斯坦 google.co.uz 乌兹别克语",
"土库曼斯坦 google.tm 土库曼语",
"阿富汗 google.com.af 波斯语",
"巴基斯坦 google.com.pk 乌尔都语",
"尼泊尔 google.com.np 尼泊尔语",
"印度 google.co.in 英语",
"孟加拉国 google.com.bd 英语",
"斯里兰卡 google.lk 僧伽罗语",
"马尔代夫 google.mv 马尔代夫语",
"科威特 google.com.kw 阿拉伯语",
"沙特阿拉伯 google.com.sa 阿拉伯语",
"巴林 google.com.bh 阿拉伯语",
"阿联酋 google.ae 阿拉伯语",
"阿曼 google.com.om 阿拉伯语",
"约旦 google.jo 阿拉伯语",
"以色列 google.co.il 阿拉伯语",
"黎巴嫩 google.com.lb 阿拉伯语",
"土耳其 google.com.tr 土耳其语",
"阿塞拜疆 google.az 阿塞拜疆语",
"亚美尼亚 google.am 亚美尼亚语英语",
"莱索托 google.co.ls 莱索托语",
"冰岛 google.is英语",
"丹麦 google.dk 丹麦语",
"挪威 google.no 挪威语",
"瑞典 google.se 瑞典语",
"芬兰 google.fi 芬兰语",
"爱沙尼亚 google.ee 爱沙尼亚语",
"拉脱维亚 google.lv 拉脱维亚语",
"立陶宛 google.lt 立陶宛语",
"爱尔兰 google.ie 爱尔兰语",
"英国 google.co.uk 英语",
"根西 google.gg",
"泽西 google.je",
"马恩 google.im",
"法国 google.fr 法语",
"荷兰 google.nl 荷兰语",
"比利时 google.be 荷兰语",
"卢森堡 google.lu 德语",
"德国 google.de 德语",
"奥地利 google.at 德语",
"瑞士 google.ch 德语",
"列支敦士登 google.li 德语",
"葡萄牙 google.pt 葡萄牙语",
"西班牙 google.es 西班牙语",
"直布罗陀 google.com.gi 西班牙语",
"安道尔 google.ad 法语",
"意大利 google.it 意大利语",
"马耳他 google.com.mt 马耳他语",
"圣马力诺 google.sm 意大利语",
"希腊 google.gr 希腊语",
"俄罗斯 google.ru 俄语",
"白俄罗斯 google.com.by 白俄罗斯语",
"乌克兰 google.com.ua 乌克兰语",
"波兰 google.pl 波兰语",
"捷克 google.cz 捷克语",
"斯洛伐克 google.sk 斯洛伐克语",
"匈牙利 google.hu 匈牙利语",
"斯洛文尼亚 google.si 斯洛文尼亚语",
"克罗地亚 google.hr 克罗地亚语",
"波黑 google.ba 塞尔维亚语",
"黑山 google.me 黑山语",
"塞尔维亚 google.rs 塞尔维亚语",
"马其顿 google.mk 马其顿语",
"保加利亚 google.bg 保加利亚语",
"罗马尼亚 google.ro 罗马尼亚语",
"摩尔多瓦 google.md 摩尔多瓦语",
"埃及 google.com.eg 阿拉伯语",
"利比亚 google.com.ly 阿拉伯语",
"阿尔及利亚 google.dz 阿拉伯语",
"摩洛哥 google.co.ma 阿拉伯语",
"塞内加尔 google.sn 法语",
"冈比亚 google.gm 英语",
"马里 google.ml 法语",
"布基纳法索 google.bf 法语",
"塞拉利昂 google.com.sl 英语",
"科特迪瓦 google.ci 法语",
"加纳 google.com.gh 英语",
"多哥 google.tg 法语",
"贝宁 google.bj 法语",
"尼日尔 google.ne 法语",
"尼日利亚 google.com.ng 英语",
"圣赫勒拿 google.sh 英语",
"喀麦隆 google.cm 法语",
"乍得 google.td 阿拉伯语",
"中非 google.cf 法语",
"加蓬 google.ga 法语",
"刚果（布） google.cg 法语",
"刚果（金） google.cd 法语",
"安哥拉 google.it.ao 葡萄牙语",
"埃塞俄比亚 google.com.et 安哈拉语",
"吉布提 google.dj 阿拉伯语",
"肯尼亚 google.co.ke 英语",
"乌干达 google.co.ug 英语",
"坦桑尼亚 google.co.tz 英语",
"卢旺达 google.rw 卢旺达语",
"布隆迪 google.bi 布隆迪语",
"马拉维 google.mw 契瓦语",
"莫桑比克 google.co.mz 葡萄牙语",
"马达加斯加 google.mg 马尔加什语",
"塞舌尔 google.sc 英语",
"毛里求斯 google.mu 英语",
"赞比亚 google.co.zm 英语",
"津巴布韦 google.co.zw 英语",
"博茨瓦纳 google.co.bw 茨瓦纳语",
"纳米比亚 google.com.na 南非荷兰语",
"南非 google.co.za",
"澳大利亚 google.com.au 英语",
"诺福克岛 google.com.nf 英语",
"新西兰 google.co.nz 英语",
"所罗门群岛 google.com.sb Pidgin",
"斐济 google.com.fj 印地语",
"密克罗尼西亚 google.fm 英语",
"基里巴斯 google.ki 吉尔伯特语",
"瑙鲁 google.nr 瑙鲁语",
"托克劳 google.tk 英语",
"萨摩亚 google.ws 英语",
"东萨摩亚 google.as 萨摩亚语",
"汤加 google.to 英语",
"纽埃 google.nu 纽埃语",
"库克群岛 google.co.ck 毛利语 法语",
"多米尼加 google.com.do 西班牙语",
"特立尼达和多巴哥google.tt",
"哥伦比亚 google.com.co 西班牙语",
"厄瓜多尔 google.com.ec 西班牙语",
"委内瑞拉 google.co.ve 西班牙语",
"圭亚那 google.gy 英语",
"秘鲁 google.com.pe 西班牙语",
"玻利维亚 google.com.bo 西班牙语",
"巴拉圭 google.com.py 西班牙语",
"巴西 google.com.br 葡萄牙语",
"乌拉圭 google.com.uy 西班牙语",
"阿根廷 google.com.ar 西班牙语",
"智利 google.cl 西班牙语",
"格陵兰 google.gl 格陵兰语",
"美国 google.com 英语",
"墨西哥 google.com.mx 西班牙语",
"危地马拉 google.com.gt 西班牙语",
"伯利兹 google.com.bz 英语",
"萨尔瓦多 google.com.sv 西班牙语",
"洪都拉斯 google.hn 西班牙语",
"尼加拉瓜 google.com.ni 西班牙语",
"哥斯达黎加 google.co.cr 西班牙语",
"巴拿马 google.com.pa 西班牙语",
"巴哈马 google.bs 英语",
"古巴 google.com.cu 西班牙语",
"牙买加 google.com.jm 英语",
"海地 google.ht",
  
]

import re 


# re.search('[a-z]+',"牙买加 google.com.jm 英语")

gugelis=[re.sub(r'[\u4e00-\u9fff]','',i) for i in gugelis]

import random
a=random.choice(gugelis)
print(1)





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
@app.route('/huoqu_youtube_channels', methods=['GET', 'POST'])
def editorData332324332423333():
  
    gugedizhitmp=random.choice(gugelis)
    driver = webdriver.Chrome(options=options)
    r=request.json
    # r['name']='中国'
    q=r['name']

    # q='china'

    import time
    aaa=time.time()

    url=f"https://www.{gugedizhitmp}/search?q=site%3Ayoutube.com/@%2F+{q}".replace(' ','')
    print('使用的url', url)
    # a1=requests.get(url)
    driver.get(url)
    # time.sleep(1)
    if 0: 
      with open('debug.html' , 'w',encoding='utf-8') as f:
        f.write(driver.page_source)
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
    driver.close()
    return jsonify(out)









if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
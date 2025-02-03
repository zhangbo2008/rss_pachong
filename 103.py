from selenium import webdriver 
from selenium import webdriver
import json
try:
  from notify import send
except:
  pass
  pass
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--blink-settings=imagesEnabled=false")

import time
aaaaa=time.time()

if 1:
    print('开始爬虫.')
    url='https://www.amazon.co.jp/gp/product/B0BSLJ52ZF?&linkCode=sl1&tag=twm1a4080-22&linkId=387fac7c4d0581478539f94f3afea1ff&language=ja_JP&ref_=as_li_ss_tl'
    
    # url='https://www.amazon.co.jp/-/zh/dp/B07911QK3X?ref_=Oct_d_otopr_d_2151901051_0&pd_rd_w=0XfJ9&content-id=amzn1.sym.1374e2a8-edae-438c-991f-c31a30021de9&pf_rd_p=1374e2a8-edae-438c-991f-c31a30021de9&pf_rd_r=8AQ8MEZB9SHYAS2DP192&pd_rd_wg=zVqZ5&pd_rd_r=fbb4971a-befc-4785-993d-0c1584e21996&pd_rd_i=B07911QK3X'
    
    # url='https://www.baidu.com'
#     cookie='session-id=358-1808349-2151563; session-id-time=2082787201l; i18n-prefs=JPY; skin=noskin; ubid-acbjp=356-2093933-0778857; lc-acbjp=zh_CN; session-token="VNXhjIlj3QO9MDcQQBTqCExCdVOgyLGUACAFc6mI9VX6XBOl1bLrjQ5nY58BEleQL0+AqKk9kWnUaTPSUKxHBkre7kTQUz9BR4PIuzCnoSSUwy7pni3dU/j9+m6WzMuRHjIrT99CUYIYP5V6zXHfSUysyOBXUmnCCs34C8kOUiPDDbSs0EAT0aLycJQ0UPCL3dtWGSsREFrpkc+E4KE1UwIalMCpo4Q2HwnD2334++7GWvGZyGRlG0XO35KpR0LAO/75V1WKSlwjaraEyingpkKGmXXSkJKhzeV9cm8tLyd/awEdH4zXQiIIE8C4vLsufYHvmoTuDxhI1mtGIbTk2nNDKlvHn/mEcRVq+tgIjFg="
# '





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
    #========循环体.
    while 1:
      import time
      # driver.get('https://www.amazon.co.jp')
      aaaaa=time.time()
      driver.get(url)
      # time.sleep(150) # 查看效果
      # if 1: 
      #   with open('debug.html' , 'w',encoding='utf-8') as f:
      #     f.write(driver.page_source)
      # driver.close()
      # a=driver.find_element(By.XPATH,'//div[@class="a-section a-spacing-none a-padding-none"]').text
      a=''
      try:
        a=driver.find_element(By.XPATH,'//span[@class="a-size-medium a-color-success"]').text
        if '有货' in a:
            name='5090'
           # send
            send(
                        title='Rakuten 发现目标商品！',
                        content=f'''商品名: {name}  
商品链接: [点击购买]({url})

---
原始链接: {url}'''
                    )
            pass
      except:
        pass
      print("结果是",a)
      print('使用时间',time.time()-aaaaa)
      import random
      time.sleep(10+random.random()*2)
    

    # 经过测试,不建议用pywright, 他里面的cookie设置的更麻烦, 并且感觉更容易失效.

    
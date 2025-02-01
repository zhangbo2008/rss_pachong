# pip install playwright
# playwright install  # 安装浏览器驱动
# 说明demo: https://scrapingant.com/blog/playwright-set-cookies
data='session-id=358-1808349-2151563; session-id-time=2082787201l; i18n-prefs=JPY; skin=noskin; ubid-acbjp=356-2093933-0778857; lc-acbjp=zh_CN; session-token="Z0Ht1a2Yxlp1XCupehP1xpl9P/t9FQAGAVnUcA93+QQcxttNRIW1c0gh2AsHP4/Cjf9O/Pu1Xb0IAri4fHeNurAAnh9CGKluJRE+8D/SOk87Jd+Ltl6OwynZwarLp/SEB5dXiGs6WaXKdQXH3SUrRcxsA3EyCsLqPapkqS0LQJamwpC0IqtR2+jVnYc+Mqu3rGZbJ8M8VU9B11UtM/y9/75OqKiokPx8tIKv50GiF2mVUBMj/bsPdSVaZmhZeiB/Pjj2oQu0brw99KEuIDqlpdzJ6umctbMf/kmBPNYSgv6E1aVv7vv1ue4wrF+VnmBIsybmD/ZVdAztE5Plp20JNdfmefcL6J2LSnDHY51L2QA="'

cookies_data = [  {
    'name': i.split('=')[0].strip(),
    'value':i.split('=')[1].strip(),
    'domain':'amazon.co.jp',
    'path': '/'
    } for  i in data.split(';')  ]




from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 启动浏览器
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # 设置 Cookie
    context.add_cookies(cookies_data)
    # context.add_cookies([
    #     {
    #         'name': 'session_id',
    #         'value': 'abc123',
    #         'domain': 'example.com',
    #         'path': '/'
    #     }
    # ])
    page = context.new_page()
    while 1:
        import time
        aaaaa=time.time()
        # 访问网页
        url='https://www.amazon.co.jp/gp/product/B0BSLJ52ZF?&linkCode=sl1&tag=twm1a4080-22&linkId=387fac7c4d0581478539f94f3afea1ff&language=ja_JP&ref_=as_li_ss_tl'
        # url='https://www.amazon.co.jp/-/zh/dp/B0DJSZKC2D?ref_=Oct_d_obs_d_2152014051_0&pd_rd_w=S1Vyi&content-id=amzn1.sym.93c56678-e2c2-4ede-8359-bb8af1f3e304&pf_rd_p=93c56678-e2c2-4ede-8359-bb8af1f3e304&pf_rd_r=Y3H0NY62Q84Y18NNRVJ3&pd_rd_wg=muaWr&pd_rd_r=35302ffa-c8cf-4ba1-9afb-b588a221a6e1&pd_rd_i=B0DJSZKC2D'
        page.goto(url)
        

        
        
        
        

        a=''
        try:
            a=page.text_content('xpath=//span[@class="a-size-medium a-color-success"]')
            # driver.find_element(By.XPATH,'//span[@class="a-size-medium a-color-success"]').text
        except:
            pass
        print("结果是",a)
        print('使用时间',time.time()-aaaaa)
        import random
        time.sleep(5+random.random()*2)
    
    
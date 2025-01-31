from selenium import webdriver

driver = webdriver.Chrome()
cookies = {"value": "value", "name": "name"}
driver.get("https://www.ketangpai.com/User/login.html")
driver.add_cookie(cookie_dict=cookies)
driver.get("https://www.ketangpai.com/Main/index.html")
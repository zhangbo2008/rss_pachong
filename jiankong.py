#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup
import os

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取上级目录
parent_dir = os.path.dirname(current_dir)
# 将notify.py所在目录添加到环境变量
os.environ["PYTHONPATH"] = parent_dir

from notify import send

def test_proxy():
    """测试代理"""
    try:
        # 获取青龙代理配置
        proxies = None
        if os.getenv('http_proxy'):
            proxy_url = os.getenv('http_proxy')
            proxies = {
                'http': proxy_url,
                'https': proxy_url
            }
            # print(f"使用代理: {proxy_url}")
        
        # 测试IP
        response = requests.get(
            'https://api.ipify.org?format=json',
            proxies=proxies,
            timeout=30
        )
        print(f"当前IP: {response.text}")
        
    except Exception as e:
        print(f"测试代理时发生错误: {str(e)}")
        if "proxy" in str(e).lower():
            print("代理连接失败，请检查代理配置是否正确")

def check_products(url,name):
    """检查商品"""
    try:
        send(
                        title='Rakuten 发现目标商品！',
                        content=f'''商品名: {name}  
商品链接: [点击购买]({url})

---
原始链接: {url}'''
                    )
        print(f"发现商品: {name}")
                    
    except Exception as e:
        print(f"检查商品时发生错误: {str(e)}")
        if "proxy" in str(e).lower():
            print("代理连接失败，请检查代理配置是否正确")

def main():
    print("开始测试代理...")
    test_proxy()
    print("\n开始监控Rakuten商品...")
    check_products()

if __name__ == "__main__":
    main()

# 当pyppeteer下载Chromium失败时运行此脚本，找出浏览器应该存储的位置，手动下载该浏览器放到相应的路径下即可，下载地址：https://registry.npmmirror.com/binary.html?path=chromium-browser-snapshots/#/

# 下载地址: https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win_x64/
 # 先配置chrome
import pyppeteer.chromium_downloader
print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))
#!!!!!!!!!我下载的是: https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win_x64/1181217/    然后复制到  C:\Users\admin\AppData\Local\pyppeteer\pyppeteer\local-chromium\1181205\chrome-win\ 即可.





import pyppeteer

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    await browser.close()
 
asyncio.get_event_loop().run_until_complete(main())













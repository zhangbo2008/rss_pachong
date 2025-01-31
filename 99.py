import  requests
a=requests.get('https://docs.rsshub.app/bilibili/user/video/2267573')
print(a.text)
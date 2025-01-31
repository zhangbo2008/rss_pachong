import re 


import re
 
text1 = "https://www.youtube.com/user/zhongguohaogequ/videos"
text2 = "https://www.youtube.com/user/kzgdiy"
text3 = "https://www.youtube.com/user/VOAchina/featured?disable_polymer=1"
match = re.match(r'https://www.youtube.com/user/(.*)/?.*', text3).group(1)
if match:
    print(match.group())
else:
    print('No match')
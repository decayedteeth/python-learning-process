import urllib.request
#response=urllib.request.urlopen('http://placekitten.com/g/500/600')
req=urllib.request.Request('http://placekitten.com/g/500/600')
#response.geturl()返回地址
#response.info()返回格式
response=urllib.request.urlopen(req)
cat_img=response.read()
with open('F://cat_500_600.jpg','wb') as f:
    f.write(cat_img)

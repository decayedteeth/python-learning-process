import urllib.request
#
# req=urllib.request.urlopen("http://www.baidu.com")
# print(req.read().decode('utf-8'))
# import urllib.parse
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

# url="http:/httpbin.org/post"
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
# }
# data=bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# url="https://www.bilibili.com"
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
# }
# req=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# url="https://www.bilibili.com"
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
# }
# data=bytes(urllib.parse.urlencode({'date':'Thu, 14 Nov 2020 11:57:58 GMT'}),encoding="utf-8")
# req=urllib.request.Request(url=url,data=data,headers=headers)
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
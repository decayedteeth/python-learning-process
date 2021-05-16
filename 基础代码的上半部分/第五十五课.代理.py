import urllib.request
url='http://www.whatismyip.com.tw'
proxy_support=urllib.request.ProxyHandler({'http':'199.6.144.73:81'})
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362')]
urllib.request.install_opener(opener)
response= urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)
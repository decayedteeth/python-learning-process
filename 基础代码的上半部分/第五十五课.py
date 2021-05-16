import urllib.parse
import urllib.request
import json
import time
while True:

    # JSON 是一种轻量级的数据交换格式，说白了这里就是用字符串把 Python 的数据结构封装起来，便与存储和使用
    content=input('请输入需要翻译的内容（输入‘!q’退出程序）:')
    if content=='!q':
        break

    url='http://fanyi.youdao.com/translate'
    '''
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
    '''
    data={}
    data['type']='AUTO'
    data['i']=content
    data['doctype']='json'
    data['xmlVersion']='1.6'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['typoResult']='true'
    data=urllib.parse.urlencode(data).encode('utf-8')

    req=urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362')
    print(req.headers)

    response=urllib.request.urlopen(url,data)
    #urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
    #url:  需要打开的网址
    #data：Post提交的数据
    #timeout：设置网站的访问超时时间
    html=response.read().decode('utf-8')
    #decode把其他编码形式变成urllib的形式


    target=json.loads(html)
    target=target['translateResult'][0][0]['tgt']
    print(target)
    time.sleep(5)

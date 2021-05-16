import urllib.request
from bs4 import BeautifulSoup

def main():
    baseurl="https://movie.douban.com/top250?start="
    datalist=getData(baseurl)
    savepath=".\\豆瓣电影TOP250.xls"
    saveData(savepath)
    askURL("https://movie.douban.com/top250?start=0")

def getData(baseurl):
    datalist=[]
    for i in range(0,10):      #获取十次网页信息
        url=baseurl+str(i*25)
        html=askURL(url)#保存获取到的网页编码

        #2.逐一解析数据
        # soup=BeautifulSoup(html,"html.parser")
        # for item in soup.find_all() #查找符合要求的字符串，形成列表


    return  datalist

def askURL(url):
    #用于伪装
    head={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
    }
    request=urllib.request.Request(url,headers=head)
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e,"code")
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(savepath):
    print("save....")

if __name__ == '__main__':
    main()
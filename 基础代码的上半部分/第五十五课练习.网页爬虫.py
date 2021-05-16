import urllib.request
import re
from bs4 import BeautifulSoup
#urllib.request打开和读取URL
#urllib.error包含urllib.request的异常
#urllib.parse用于解析URL

#read()返回服务器的元素数据
#再用decode()来解码
#Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码
def main():
    url = "http://baike.baidu.com/view/284853.htm"
    response = urllib.request.urlopen(url)
    html=response.read()
    soup = BeautifulSoup(html, "html.parser")
    #使用了Python默认的解析器
    for each in soup.find_all(href=re.compile("view")):
        print(each.text, "->", ''.join(["http://baike.baidu.com", each["href"]]))
        #上边用join()不用+直接拼接，是因为join()被证明执行效率要高很多
if __name__=="__main__":
    main()

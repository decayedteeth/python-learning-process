import re
import bs4
import xlwt
import urllib.request
from bs4 import BeautifulSoup


def mian():
    #主函数
    baseurl="https://book.douban.com/top250?start="
    datalist=[]
    getdata(baseurl,datalist)
    #1.爬取网页
    savepath=".\\豆瓣top.xls"
    saveData(savepath,datalist)
    # askURL("https://book.douban.com/top250?start=0")

# 书详情链接的规则
findLink =  re.compile(r'<a class="nbg" href="(.*?)">',re.S)   #生成正则表达式对象，表示规则（字符串的模式）
# 书图片
findImgSrc  =re.compile(r'<img src="(.*?)" width="90"/>',re.S) #re.S让换行符包含在字符中
#中文书名
findCTitle=re.compile(r'<div class="pl2">(.*?)</a>',re.S)
#英文书名
findOTitle=re.compile(r'<span style="font-size:12px;">(.*)</span>')
#书评分
findRating=re.compile(r'<span class="rating_nums">(.*)</span>')
#评价人数
findJudge=re.compile(r'<span class="pl">(.*?)</span>',re.S)
#找到概述
findIng=re.compile(r'<span class="inq">(.*?)</span>',re.S)
#作者
findHD=re.compile(r'<p class="pl">(.*?)</p>')
# .*?表示中间有若干个字符



#爬取网页
def getdata(baseurl,datalist):
    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askURL(url)
        # 2.逐一解析数据
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('tr',class_="item"):#查找符合要求的字符串
            # print(item) #查看p12的全部信息
            data=[]  #保存书的全部信息
            item = str(item)
            # link :书详情的链接
            link=re.findall(findLink,item)[0]  #re库用来通过正则表达式来查找指定的字符串
            link=re.sub('" onclick="moreurl(.*?)(this,)'," ",link)
            link=re.sub("{i:'(.*?)'}","",link)
            link=re.sub("\)","",link)
            data.append(link)#添加链接
            # print(link)

            imgSrc = re.findall(findImgSrc,item)
            if len(imgSrc)!=0:
                imgSrc=imgSrc[0]
                data.append(imgSrc)
            else:
                data.append(' ')
            # print(imgSrc)
            #添加图片


            Ctitles=re.findall(findCTitle,item)[0]
            Ctitles=re.sub('<a href="(.*?)" onclick=',"",Ctitles)
            Ctitles=re.sub('"&quot;moreurl(.*?)&quot;" title="(.*?)">',"",Ctitles)
            Ctitles=re.sub('<span(.*?)</span>',"",Ctitles)
            # print(Ctitles.strip())
            data.append(Ctitles.strip())
            # 添加中文书名

            # Otitle=re.findall(findOTitle,item)
            # if len(Otitle)!=0:
            #     data.append(Otitle[0])
            # else:
            #     data.append("")
            # print(Otitle)
            # #添加英文名


            rating=re.findall(findRating,item)[0]
            # print(rating)
            data.append(rating)
            #评分

            judge=re.findall(findJudge,item)
            if len(judge)!=0:
                judge=judge[0]
                judge=re.sub('\(','',judge)
                judge=re.sub('\)','',judge)
                # judge=re.sub('人评价','',judge)
                # print(judge.strip())
                data.append(judge.strip())#添加评价人数
            else:
                data.append(' ')
            #


            ing=re.findall(findIng,item)
            if len(ing)!=0:
                ing=ing[0]
                data.append(ing) 
            else:
                data.append(' ')
            # print(ing)

            #添加概述

            hd=re.findall(findHD,item)[0]
            # print(hd)
            data.append(hd)

            datalist.append(data)  #处理好书信息放入datalist
            # print(link)
            # print(imgSrc)
    # print(datalist)





    return datalist
    #返回网址的数据
# 得到指定的URL网页信息
def askURL(url):
    head={#模拟浏览器头部信息，发送消息
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19041"
    }   #用于伪装服务器
    request=urllib.request.Request(url,headers=head)
    #发送请求
    try:
        response=urllib.request.urlopen(request)
        #打开网址,响应
        html=response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e,"code")
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def saveData(savepath,datalist):
    # print(datalist)
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=book.add_sheet('豆瓣图书top250',cell_overwrite_ok=True)
    col=('图书详情链接',"图片链接","图书中文名","评分","评分人数","概况","相关信息")
    for i in range(0,7):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print('第%d条'%(i+1))
        data=datalist[i]
        for j in range(0,7):
            sheet.write(i+1,j,data[j])
    print('打印成功')
    book.save(savepath)
    # 3.保存数据


if __name__ == '__main__':#自动调用自身
    mian()
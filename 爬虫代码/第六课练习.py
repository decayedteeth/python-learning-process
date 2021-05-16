import re
from bs4 import BeautifulSoup
import urllib.request
import xlwt


def main():
    # 主函数
    baseurl="https://movie.douban.com/top250?start="
    # 爬取网页
    datalist=[]
    getdata(baseurl,datalist)
    #保存数据

    savepath = ".\\豆瓣top.xls"
    saveData(datalist,savepath)
    # askURL("https://movie.douban.com/top250?start=0")

# .*?表示中间有若干个字符
findLink=re.compile(r'<a href="(.*?)">')
#电影链接
findImg=re.compile(r'<img alt=(.*?).jpg" width="100"/>',re.S)
#电影图片
# re.S让换行符包含在字符中
findTitle=re.compile(r'<span class="title">(.*?)</span>')
#电影标题
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#电影评分
findJudgenum=re.compile(r'<span>(.*?)</span>')
#评价人数
findIng=re.compile(r'<span class="inq">(.*?)</span>')
#概述
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
#re.S忽视换行符
#导演和类型
# (.*)只出现0次到一次
# (.*)?出现0次到多次


# 爬取网页
def getdata(baseurl,datalist):
    # datalist = []
    #创建一个集合来保存数据
    for i in range(0,10):
        url=baseurl+str(i*25)+str('&filter=')
        html=askURL(url)
        #逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串
            # print(item)
            data = []  # 保存电影的全部信息
            item=str(item)


            link = re.findall(findLink,item)[0]  # re库用来通过正则表达式来查找指定的字符串
            # print(link)
            data.append(link)  # 添加链接

            imgSrc= re.findall(findImg,item)[0]
            imgSrc= imgSrc.replace('class="" src=',"  ")
            data.append(imgSrc)

            titles=re.findall(findTitle,item)
            if(len(titles)==2):
                ctitle=titles[0]
                data.append(ctitle)
                otitle=titles[1].replace("\xa0/\xa0"," ")
                data.append(otitle)
            else:
                ctitle=titles[0]
                data.append(ctitle)
                data.append(' ')

            rating=re.findall(findRating,item)[0]
            data.append(rating)

            judgenum=re.findall(findJudgenum,item)[0]
            data.append(judgenum)

            ing=re.findall(findIng,item)
            if len(ing)!=0:
                ing=ing[0].replace("。","")
                data.append(ing)
            else:
                data.append('')

            bd=re.findall(findBd,item)[0]
            bd=re.sub("<br/(\s+)?>(\s+)?"," ",bd)
            #去掉<br/> <br/>是换行符
            bd=re.sub('/'," ",bd)
            bd=re.sub('\xa0'," ",bd)
            # (s+)?表示存在一个或者多个
            data.append(bd.strip())  #去掉前后空格




            datalist.append(data)
    # print(datalist)
    return datalist


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




def saveData(datalist,savepath):#保存数据

    # print(datalist)
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)#创建工作对象
    sheet=book.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)#创建工作表
    col=('电影详情链接',"图片链接","影片中文名","影片外文明","评分","评分人","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])#列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    print('爬取成功')
    book.save(savepath)

if __name__ == '__main__':
    main()
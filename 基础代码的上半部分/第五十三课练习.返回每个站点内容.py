import urllib.request
import chardet
#URL的意思是网址
def main():
    i=0
    with open("F:/PYTHON/url.txt","r") as f:
        #读取待访问的网址
        #由于urls.txt每一行一个 URL
        #所以按换行符'\n'分割
        urls=f.read().splitlines()
    for each_url in urls:
        response=urllib.request.urlopen(each_url)
        html=response.read()
        #识别网页编码
        encode=chardet.detect(html)['encoding']
        if encode=='GB2312':
            encode='GBK'
        i+=1
        filename="url_%d.txt"%i
        with open(filename,"w",encoding=encode) as each_file:
            each_file.write(html.decode(encode,"ignore"))
if __name__=="__main__":
    main()

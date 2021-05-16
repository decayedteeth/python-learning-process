import urllib.request
import chardet
def main():
    url=input("请输入URL:")
    response=urllib.request.urlopen(url)
    html=response.read()
    #识别网页编码
    encode=chardet.detect(html)['encoding']
    if encode=='GB2312':
        encode='GRK'
        print("该网页使用的编码是:%s"% encode)
        #py文件被直接运行时，if __name__ == '__main__'之下的代
       # 码块将被运行；当.py文件以模块形式被导入时，if
        #__name__ == '__main__'之下的代码块不被运行。
if __name__=="__main__":
    main()

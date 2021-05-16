import easygui as g
import os
file_path =g.fileopenbox(default="*.txt")#default是对文件类型的描述
#fileopenbox(msg=None,title=None,default='*',filetypes=None)
#filetypes可以选择多种文件类型，但是在这里如果选default就只会出现.txt的后缀
with open(file_path) as f:
    title = os.path.basename(file_path)#basename返回目录路径中的最后一个元素
    #如print(basename('abc/123.dat')) 输出为123.dat
    msg="文件[%s]的内容如下："%title
    text =f.read()#.read只读
    g.textbox(msg,title,text)#textbox文本框

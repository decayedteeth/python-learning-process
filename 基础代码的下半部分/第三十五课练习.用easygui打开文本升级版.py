import easygui as g
import os
file_path =g.fileopenbox(default="*.txt")#default是对文件类型的描述
#fileopenbox(msg=None,title=None,default='*',filetypes=None)
#filetypes可以选择多种文件类型，但是在这里如果选default就只会出现.txt的后缀
with open(file_path) as old_file:
    title=os.path.basename(file_path)
    msg="文件[%s]的内容如下:"%title
    text=old_file.read()
    text_after=g.textbox(msg,title,text)
if text!=text_after[:-1]:
    #[:-1]指的是0到-1的值
    choice=g.buttonbox("检测到文件内容发生改变,请选择以下操作:","警告",
                       ("覆盖保存","放弃保存","另存为..."))
    #buttonbox定义自己的一组按钮
    #buttonbox(msg='',title='',choice=(Button[1]))
    if choice =="覆盖保存":
        with open (file_path,"w")as old_file:
            old_file.write(text_after[:-1])
    if choice =="放弃保存":
        pass
    if choice == "另存为...":
        another_path=g.filesavebox(default=".txt")
        #filesavebox保存一个文件,并选择路径,default是它的后缀
        if os.path.splitext(another_path)[1]!='.txt':
            another_path+='.txt
            #spiltext更更多用于搜索文件路径和文件扩展名和spilt主要用于字符串'
        with open(another_path,"w") as new_file:
            new_file.write(text_after[:-1])

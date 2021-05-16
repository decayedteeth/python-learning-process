import easygui as g
import os
def show_result(start_dir):#显示结果
    lines=0
    total=0
    text=""
    for i in source_list:
        lines=source_list[i]
        total+=lines
        text+="[%s]源文件%d个，源代码%d行\n"%(i,file_list[i],lines)
    title='统计结果'
    msg='您目前共积累编写了%d行代码,完成度:%.2f %%\n离10万行代码还差%d行，请继续努力！'%(total,total/1000,100000-total)
    g.textbox(msg,title,text)
def calc_code(file_name):#分析文件
    lines=0
    with open(file_name) as f:
        print('正在分析文件：%s...'% file_name)
        try:
            for each_line in f:
                lines+=1
        except UnicodeDecodeError:
            pass
    return lines
def search_file(start_dir):#打开文件夹   
    os.chdir(start_dir)#chdir用于改变当前工作的路径
    for each_file in os.listdir(os.curdir):#curdir只的是当前目录
        ext=os.path.splitext(each_file)[1]#ext取文件的后缀
        if ext in target:
            lines=calc_code(each_file)
            #统计行数
            try:
                file_list[ext]+=1
            except KeyError:
                file_list[ext]=1
            try:
                source_list[ext]+=lines
            except KeyError:
                source_list[ext]=lines
        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)
target=['.c','.cpp','py','.cc',',java','.pas','.asm']
file_list={}
source_list={}
g.msgbox("请打开你存放所有代码的文件夹...","统计代码量")
#第一个输出
path=g.diropenbox("请选择您的代码库：")#diropenbox
search_file(path)#寻找文件..
show_result(path)

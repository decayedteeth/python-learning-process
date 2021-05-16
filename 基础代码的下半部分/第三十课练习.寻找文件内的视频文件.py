import os#该代码适用于多个操作系统
def search_file(start_dir,targer):
    os.chdir(start_dir)#os.chdir用来改变当前工作目录到指定路径
    for each_file in os.listdir(os.curdir):#列举出当前目录的所肉文件
        ext=os.path.splitext(each_file)[1]#把文件的后缀赋值到ext上
        if ext in target:#若ext中有mp4......
            vedio_list.append(os.getcwd()+os.sep+each_file+os.linesep)
            #getcwd()返回当前工作目录,
            #os.sep是分割符,如C:\User\Deskerp  '\'就是os.sep
            #os.linesep字符串给出当前平台使用和行终止符
        if os.path.isdir(each_file):#判断对象是否是一个目录
            search_file(each_file,target)
            os.chdir(os.pardir)#paddir指代上一级目录
            #改变当前工作目录到上一级 
start_dir=input('请输入待查找的初始目录,输入格式为  例：F:\文件名：')
program_dir=os.getcwd()#getcwd()返回当前工作目录
target=['.mp4','.avi','.rmvb']
vedio_list=[]
search_file(start_dir,target)
f=open(program_dir+os.sep+'vediolist.txt','w')#创建一个文件存放路径
f.writelines(vedio_list)#writelines用于向文件中写入义序列字符串
f.close()

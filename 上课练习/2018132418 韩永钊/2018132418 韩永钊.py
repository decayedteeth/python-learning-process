import os
print('-----------课程管理系统----------')
print('         1.添加课程信息')
print('         2.删除课程信息')
print('         3.查询课程信息')
print('         4.保存课程信息数据')
print('         5.打开课程信息数据')
print('         0.退出系统')
L=[]
def add_new_class():
    while 1:        
        num=input('请输入新课程的编号：')
        #num编号
        c=input('请输入新课程的名称：')
        #c名称
        t=input('请输入新课程的类型（专业课/基础课）：')
        #t类型
        s=input('请输入新课程的学分')
        #s:学分
        ti=input('请输入新课程的学时')
        #ti时间
        dict1={}
        dict1["number"]=num
        dict1["class"]=c
        dict1["type"]=t
        dict1["score"]=s
        dict1["time"]=ti
        L.append(dict1)
        print("增加成功")
        print('--------处理后的数据---------')
        print("课程编号"+'     '+"课程类型"+'     '+'课程学分'+'     '+'课程课时'+'     '+'课程名称')
        for item in L:  
            print('  ',item['number'],'       ',item['type'],'         ',item['score'],'         ',item['time'],'         ',item['class'])
        break

def del_class():
    del_number=input('请输入需要删除的课程编号')
    find_flag=False
    for line in L:
        if line['number']==del_number:
            L.remove(line)
            find_flag=True
        else:
            find_flag=False
    if find_flag:
        print("已经删除")
    else:
        print('输入的不存在或删除失败')
    print('--------处理后的数据---------')
    print("课程编号"+'  '+"课程类型"+'    '+'课程学分'+'     '+'课程课时'+'     '+'课程名称')
    for item in L:
        print('   ',item['number'],'         ',item['type'],'         ',item['score'],'         ',item['time'],'         ',item['class'])
def find_class():
    find_number=input('请输入需要查找的课程编号')
    find_infors=0
    for item in L:
        if find_number in item['number']:
            print('--------恭喜你,数据查找成功---------')
            print("课程编号"+'     '+"课程类型"+'     '+'课程学分'+'     '+'课程课时'+'     '+'课程名称')
            print('   ',item['number'],'        ',item['type'],'         ',item['score'],'         ',item['time'],'         ',item['class'])
            find_infors = 1
            break
    if find_infors == 0:
        print('找不到该课程号')
def save_class():
    f=open('F:/PYTHON/上课练习/2018132418 韩永钊/record.txt','w+')
    f.write("课程编号"+'     '+"课程类型"+'     '+'课程学分'+'     '+'课程课时'+'     '+'课程名称\n')
    for item in L:
        s=(item['number'],item['type'],item['score'],item['time'],item['class'])
        a=str(s)
#    for line in range(len(L)):
#        s=str(L[line]),replace('[','').replace(']','')
#        s=s.replace("'",''),f.replace(',','')+'\n'
        f.write(a)
    f.close()
    print('--------恭喜你,数据存储完成---------')
    print('--------处理后的数据---------')
    print("课程编号"+'     '+"课程类型"+'     '+'课程学分'+'     '+'课程课时'+'     '+'课程名称')
    for item in L:
        print('   ',item['number'],'         ',item['type'],'         ',item['score'],'         ',item['time'],'         ',item['class'])
def display_class():
    print('--------处理后的数据---------')
    print("课程编号"+'     '+"课程类型"+'     '+'课程学分'+'     '+'课程课时'+'     '+'课程名称')
    for item in L:
        print('   ',item['number'],'         ',item['type'],'         ',item['score'],'         ',item['time'],'         ',item['class'])
def main():
    while 1:
        n=int(input('请输入功能对应的数字'))
        if n==1:
            print('--------欢迎使用添加功能---------')
            add_new_class()
        elif n==2:
            print('--------欢迎删除添加功能---------')
            del_class()
        elif n==3:
            print('--------欢迎查询添加功能---------')
            find_class()
        elif n==4:
            save_class()
        elif n==5:
            print('--------恭喜你,打开数据成功---------')
            display_class()
        elif n==0:
            n=input('确定退出吗？(YES/NO):')
            if n=='YES' or n=='yes':
                break
            else:
                continue
        else:
            print('输入错误,请重新输入')
main()

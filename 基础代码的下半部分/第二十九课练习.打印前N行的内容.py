def file_view(file_name,line_num):
    print('\n文件%s的前%s行的内容如下:\n'%(file_name,line_num))
    f=open(file_name)#要打开的文件
    for i in range(int(line_num)):
        print(f.readline(),end='')#readline是每次读取一行内容
#输出前line_num行的内容
    f.close()

file_name =input('请输入要打开的文件名')
line_num=input('请输入需要显示文件的前几行：')
file_view(file_name,line_num)

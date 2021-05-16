def file_write(file_name):
    f = open(file_name,'w') #'w'是指这个文件可写，打开定义的文件
    print('请输入内容[单独输入\':w\'保存退出]:')

    while True:#永远循环
        write_some = input()
        if write_some !=':w':#若输入不是:w就继续
            f.write('%s\n'% write_some)
        else:
            break

    f.close()

file_name=input('请输入文件名：')#文件的名字
file_write(file_name)

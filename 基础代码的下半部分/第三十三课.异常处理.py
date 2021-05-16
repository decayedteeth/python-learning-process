try:
    f=open('file.txt')
    print(f.read())
    f.close()
except OSError as reason:#OSError指的是系统产生的异常,(如打开一个不存在的文件)
    #这里的OSError可以是其他错误类型
    #格式为 'expect Exception[as reason]'Exception指的是异常处理代码
    print('文件出错了\n错误的原因是:'+str(reason))

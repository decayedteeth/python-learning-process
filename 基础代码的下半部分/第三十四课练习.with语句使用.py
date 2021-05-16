try:
    with open('data.txt','w')as f:#这里使用with就算忘记关闭文件也没关系
        for each_line in f:
            print(each_line)
except OSError as reason:#OSError是操作系统产生异常，比如打开一个不存在的文件
    print('出错了:'+str(reason))

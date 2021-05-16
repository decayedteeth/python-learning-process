try:
    for i in range(3):
        for j in range(3):
            if i==2:
                raise KeyboardInterrupt#引发一个异常
            print(i,j)
except KeyboardInterrupt:#若发生KeyboardInterrupt异常，（已经在raise引发）
    print('退出了')

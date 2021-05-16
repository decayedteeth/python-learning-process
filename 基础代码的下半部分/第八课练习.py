temp=input('输入分数')
i=int(temp)
if 90<i<=100:
    print('A',end='')
elif 80<i<=90:
    print('B',end='')
elif 70<i<=80:
    print('C',end=' ')
elif 0<=i<=70:
    print('D',end='')
elif i:
    print('输出错误 ')

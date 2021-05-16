temp= input('请输入一个整数')
lily=int(temp)
while lily:
    k=lily-1
    while k:
        print(' ',end='')
        k=k-1
        j=lily
        while j:
            print('*',end='')
            j=j-1
            print()
            lily=lily-1

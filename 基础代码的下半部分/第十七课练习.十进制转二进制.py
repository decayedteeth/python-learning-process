def Dec2Bin(dec):
    temp=[]
    result=''
    while dec:
        quo=dec%2
        dec=dec//2#   '%'是取余   '//'是整除 例：11//2=5
        temp.append(quo)

    while temp:
        result+=str(temp.pop())

    return result


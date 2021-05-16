def age(n):
    if n==1:
        return 10 若age(1)=10
    else :
        return age(n-1)+2#若n==5，age(5)=age(4)+2,age(4)=age(3)+2
    
n=int(input('输入第n的人的年龄'))
print('第%s的年龄是%s'% (n,age(n)))

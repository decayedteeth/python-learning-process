def fun(n):
    if n==1:
        return 1
    else:
        return n*fun(n-1)#若传入的是5，则是fun(5*fun(4*fun(3*fun(2*fun(1)))))
    #递归的条件：1.有调用自身的行为
    #2.有一个正确的返回条件

number=int(input('请输入一个数'))
result=fun(number)
print("%d的阶乘是%d" %(number,result))

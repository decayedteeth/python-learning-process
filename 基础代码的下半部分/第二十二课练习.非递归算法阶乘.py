def factorial(n):#非递归算法1
    result =n
    for i in range(1,n):
        result*=i

    return result
n=int(input('请输入一个数:'))
print("%d 的阶乘是:%d" %(n,factorial(n)))

x=int(input('请输入一个数:'))#非递归算法2
result=1
while x:
    result*=x
    x-=1
print(result)



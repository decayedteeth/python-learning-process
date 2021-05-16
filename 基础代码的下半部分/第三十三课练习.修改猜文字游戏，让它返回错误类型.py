import random
secret=random.randint(1,10)
print("猜数字")
temp=input("输入数字")
try:
    guess=int(temp)#判断输入的值是否是int类型
except(ValueError):#'ValueError'检测用户传入无效参数
    print('你输入的有问题')#发生错误的时候输出...
    temp=input('请重新输入')#重新输入temp
    guess=int(temp)
finally:#'finally'无论如何也会继续执行
    if guess ==secret:
        print("输入正确")
    while guess !=secret: 
        if guess > secret:
                print("大了")
        else:
                print("小了")
        temp=input("重新输入\n")
        guess=int(temp)
    print("游戏结束")

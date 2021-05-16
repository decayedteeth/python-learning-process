import random
serect=random.randint(1,10)
print("猜数字")
temp=input("输入数字")
guess=int(temp)
if guess ==serect:
    print("输入正确")
while guess !=serect: 
    if guess > serect:
            print("大了")
    else:
            print("小了")
    temp=input("重新输入\n")
    guess=int(temp)
print("游戏结束")

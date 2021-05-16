import easygui as g
import random

g.msgbox("海，欢迎进入第一个页面小游戏")
secret=random.randint(1,10)

msg ="不妨猜一下小甲鱼现在心里想的是什么数字"
title="数字小游戏"
guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)
#这里的lowerbound和upperbound限定了最大最小值
while 1:
    if guess==secret:
        g.msgbox("猜中了")
        g.msgbox("猜中了也没有奖励")
        break
    else:
        if guess>secret:
            g.msgbox("大了")
        else:
            g.msgbox("小了")
        guess =g.integerbox(msg,title,lowerbound=1,upperbound=10)#guess不变
g.msgbox("游戏结束")

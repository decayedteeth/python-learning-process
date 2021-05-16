import easygui as g
import sys
while 1:
    g.msgbox ('欢迎进入第一个游戏小界面')#
    msg='请问你希望在C工作室学到什么东西？'
    title="小游戏互动"
    choices=["谈恋爱","编程","OOXX","琴棋书画"]
    choice=g.choicebox(msg,title,choices)#choicebox可以接受好几个参数
    g.msgbox("你的选择是："+str(choice),"结果")#结果是title easygui可以接受
    #关键字参数
    msg="你希望重新开始游戏吗"
    title='请选择'
    if g.ccbox(msg,title):#ccbox提供一个选择:Continue或者Cancel，并返回相应的值
        #0或1
        #可修改成g.ccbox(msg,choices=("是","否"))
        pass
    else:
        sys.exit(0)

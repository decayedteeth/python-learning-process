import easygui as g
import random as r
import sys
symbols=r'''!@#$%^&*()_+-=/*[]{}\''';?,.<>'''
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums='0123456789'
  #  print('--欢迎进入吃鱼游戏--')
  #  print('--登录游戏--')
  #  print('-输入已有用户名和密码-')
   # print('--注册新的用户名和密码--')
  #  print('--开始游戏--')
   # print('--打印结果--')

g.msgbox('欢迎进入吃鱼游戏')
title="登录游戏"
msg="是否有账号"
choices=["登录账号","注册账号","退出游戏"]
user=dict()#创建一个新的字典,用来储存账号密码
while 1:
    choice=g.buttonbox(msg,title,choices)#给用户选择三个选项
    if choice =="登录游戏":
        
    if choice =="注册账号":#如果选择'注册账号'
            #创建一个字典来储存账号密码，并在分密码登记
        account=input('请输入账号')
        if account in user:
            g.msgbox('该账号已被注册')
        else:
            msg="您的密码需要符合:  \n\
        \t1. 密码必须数字,字母及特殊字符三种组成     \n\
        \t2. 密码只能由字母开头  \n\
        \t3. 密码长度不能低于8位"
            title="输入密码"
            while 1:
                password=g.passwordbox(msg,title)
                length=len(password)
                while (password.isspace() or length==0):
                        g.msgbox("您输入的密码为空，请重新输入")
                        password=g.passwordbox(msg,title)
                        length=len(password)
                if length<=4:
                    flag_len=1
                elif 4<length<8:
                    flag_len=2
                else:
                    flag_len=3
                flag_con=0
                for each in password:
                    if each in symbols:
                        flag_con +=1
                        break
                for each in password:
                    if each in nums:
                        flag_con +=1
                        break
                for each in password:
                    if each in chars:
                        flag_con+=1
                        break
                if flag_len==1 or flag_con==1:
                    g.msgbox("您输入的密码太简单,请重新输入")
                elif flag_len==2 or flag_con==2:
                    g.msgbox("您输入的密码太简单,请重新输入")
                else:
                    g.msgbox("宁输入的密码符合规范\n注册成功")
                    break
            user[account]=password
    if choice =="退出游戏":
        break


    



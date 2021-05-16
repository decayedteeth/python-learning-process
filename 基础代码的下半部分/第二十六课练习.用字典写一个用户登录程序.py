while 1:
    user_data={}
    print('''---新建用户:N/n---''')
    print('''---登录账号:E/e---''')
    print('''---退出程序:Q/q---''')
    A=input('---请输入指令代码:')

    if A=='N' or A=='n':
        while 1:
            name=input('请输入用户名:')
            if name in user_data:
                print('此用户名已经存在，请重新输入:')
                continue
            else:
                break
        password=input('请输入密码:')
        user_data.setdefault(name,password)
        print('注册成功')

    elif  A=='E' or A=='e':
        while 1:
            name=input('请输入用户名:')
            if name not in user_data:
                print('该用户不存在,请重新输入:')
                continue
            else:
                break
        password=input('请输入密码:')
        pwd = user_data.get(name)
        if passowrd==pwd:
            print('欢迎进入XX系统,点击右上角的X结束程序!')
        else:
            print('密码错误!')

    elif A=='Q' or A=='q':
        print('感谢您的使用')
        break

    else:
        print('输入有误,请重新输入')
        

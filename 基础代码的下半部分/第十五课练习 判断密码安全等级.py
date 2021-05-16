symbols=r'''!@#$%^&*()_+-=/*[]{}\''';?,.<>'''
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums='0123456789'
while 1:
    passwd=input('请输入检查的密码组合：')

    length=len(passwd)
    while(passwd.isspace() or length==0):
        passwd=input("您的输入密码为空，请重新输入：")
        length=len(passwd)
    if length<=8:
        flag_len=1
    elif 8<length<16:
        flag_len=2
    else:
        flag_len=3
    flag_con=0
    for each in passwd:
        if each in symbols:
            flag_con+=1
            break
    for each in passwd:
        if each in chars:
            flag_con+=1
            break
    for each in passwd:
        if each in nums:
            flag_con+=1
            break
    print("您的安全等级评定为： "  )
    if flag_len==1 or flag_con==1:
        print("低")
        print('请按以下方式提升您的密码安全等级:  \n\
        \t1. 密码必须数字,字母及特殊字符三种组成     \n\
        \t2. 密码只能由字母开头  \n\
        \t3. 密码长度不能低于16位')
        print("请重新输入")
    elif flag_len==2 or flag_con==2:
        print("中")
        print('请按以下方式提升您的密码安全等级:  \n\
        \t1. 密码必须数字,字母及特殊字符三种组成     \n\
        \t2. 密码只能由字母开头  \n\
        \t3. 密码长度不能低于16位')
        print("请重新输入")
    else:
        print("高")
        print("请继续保持")
        break
    


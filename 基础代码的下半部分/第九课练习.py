count =3
password='CC'

while count:
    passwd=input('请输入密码')
    if passwd==password:
        print('输入正确')
        break
    elif '*' in passwd:
        print('不能包含*，还有',count,'次机会')
        continue
    else:
        print('密码错误，还有',count,'次机会')
        count-=1
#countine是不执行下面的代码，重新返回循环，break是终止循环

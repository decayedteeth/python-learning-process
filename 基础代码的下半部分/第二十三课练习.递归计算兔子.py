def fab(n):
    if n<1:
        print('输入有误！')
        return -1
    if n==1 or n==2:
        return 1
    else :
        return fab(n-1)+fab(n-2)#公式F(n)=F(n-1)+f(n-1),n>2

n=int(input('请输入一个数:'))
if n !=-1:
    print('有%d只小兔子出生'% fab(n))

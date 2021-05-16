x=list(filter(lambda n:not(n%3),range(1,100)))#'filter用来筛选，把不合适
#的元素过滤掉'
print(x)


def odd(b):#把lambda拆开后
    return b%3==0
temp=range(1,100)
y=filter(odd,temp)#filter把不是3整除的筛选掉
print(list(y))

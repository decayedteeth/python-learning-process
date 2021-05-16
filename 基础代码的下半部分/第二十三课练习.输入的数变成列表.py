result=[]
def get_digits(n):
    if n>0:
        result.insert(0,n%10)#在get_digits列表里面增加n的余数
        get_digits(n//10)#get_digits整除10

n=int(input('输入一个数'))
get_digits(n)
print(result)

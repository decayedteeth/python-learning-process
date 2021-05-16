def funX():
    x=5
    def funY():
        nonlocal x#'nonlocal'可以修改内部函数的局部变量
        x+=1
        return x
    return funY

a=funX()
print(a())#6
print(a())#7
print(a())#8

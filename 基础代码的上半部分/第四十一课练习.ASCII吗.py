class Nint(int):
    def __new__(cls,arg=0):
        if isinstance(arg,str):
            #判断如果是字符串
            #isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
            total=0
            for each in arg:
                total += ord(each)
                #ord()可以返回相应的ASCII函数
            arg = total
        return int.__new__(cls,arg)
    #self表示的是一个具体的实例本身
    #cls表示的是类本身体

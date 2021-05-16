#class Nstr(int):
#    def __new__(cls,arg=0):
#        if isinstance(arg,str):
#            #判断如果是字符串
 #           #isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
#            total=0
#            for each in arg:
#                total += ord(each)
#                #ord()可以返回相应的ASCII函数
 #           arg = total
#        return int.__new__(cls,arg)
class Nstr:
    def __init__(self,arg=''):
        if isinstance(arg,str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误")
    def __add__(self,other):
        return self.total+other.total
    def __sub__(self,other):
         return self.total-other.total
    def __mul__(self,other):
        return self.total * other.total
    def __truediv__(self,other):
        return self.total /other.total
    def __floordiv__(self,other):
        return self.total//other.total
a=Nstr('LOve c')
b=Nstr('ssd')

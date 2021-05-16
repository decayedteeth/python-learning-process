class Celsius:
    def __init__(self,value=26.0):
        self.value=float(value)
    def __get__(self,instance,owner):#用于访问属性，返回属性的值
        return self.value
    def __set__(self,instance,value):#当属性分配操作中调用，不返回任何内容
        self.value=float(value)
class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel *1.8+32
    def __set__(self,instance,value):
        instance.cel=(flaot(value)-32)/1.8
class Temperature:
    cel = Celsius()
    fah=Fahrenheit()
    

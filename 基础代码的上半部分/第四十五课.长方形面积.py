class R:
    def __init__(self,width=0,height=0):
        self.width=width
        self.height=height
    def __setattr__(self,name,value):
        if name=="square":#这个是正方形
            self.width=value
            self.height=value
        else:
            super().__setattr__(name,value)
            #self__dict__[name]=value 方法二
            #self.name=value 错误：会进入死循环
    def getArea(self):
        return self.width*self.height

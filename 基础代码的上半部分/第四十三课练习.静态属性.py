class C:
    count =0#静态属性
    #静态属性就是没有self
    def __init__(self):
        C.count=C.count +1
        #这里原来是self.count但是静态属性可以直接用类
    def getCount(self):
        return C.count

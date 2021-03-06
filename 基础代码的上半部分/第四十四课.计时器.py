import time as t
class MyTimer():
    def __init__(self):
        self.unit=['年','月','日','分钟','秒']#类属性
        self.prompt="未开始计时！"
        self.lasted=[]
        self.begin=0
        self.end=0
    def __str__(self):#这里是调用实例对象的时候回出现
        return self.prompt
    __repr__=__str__
    def __add__(self,other):
        prompt="共运行了"
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=(str(result[index])+self.unit[index])
        return prompt
    #开始计时
    def start(self):
        self.begin=t.localtime()
        self.prompt='调用stop停止计时'
        print("计时开始")
    #停止计时
    def stop(self):
        if not self.begin:
            print('先调用start')
        else:
            self.end=t.localtime()
            self._calc()
            print("计时结束")
    #计算运行时间
    def _calc(self):#这里的_calc是内部函数，只有内部可以调用，除非用global
        self.lasted=[]
        self.prompt="一共运行了"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:#为0不显示
                self.prompt+=(str(self.lasted[index])+self.unit[index])
        self.begin=0
        self.end=0
 


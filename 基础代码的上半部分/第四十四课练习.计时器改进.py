import time as t
class MyTimer:
    def __init__(self):
        self.unit=['年','月','日','小时','分钟','秒']
        self.borrow=[0,12,31,24,60,60]
        self.prompt="未开始计时"
        self.lasted=[]
        self.begin=0
        self.end=0       
    def __str__(self):#若这里直接输入实例函数这会返回prompt
        return self.prompt
    __repr__=__str__
    def __add__(self,other):#若两个计时加在一起
        prompt="一共运行了"
        result=[]
        for index in range(6):
            result.append(self.lasted[index])
            if result[index]:
                prompt+=(str(result[index])+self.unit[index])
        return prompt
    def start(self):
        self.begin = t.localtime()
        self.prompt="先用stop停止计时"
        print("计时开始")
    def stop(self):
        if not self.begin:
            print("先用start函数")#若没有调用start
        else:
            self.end=t.localtime()
            self._calc()
            print("计时结束")
    def _calc(self):
        self.lasted=[]
        self.prompt='一共运行了'
        for index in range(6):
            temp= self.end[index]-self.begin[index]
            if temp<0:#若出现负数
                i=1
                while self.lasted[index-i]<1:
                    self.lasted[index-i]+=self.borrow[index]-1
                    self.lasted[index-i-1]-=1
                    i+=1
                self.lasted.append(self.borrow[index]+temp)
                self.lasted.append(temp)
            else:
                self.lasted.append(temp)
        for index in range(6):
            if self.lasted[index]:
                self.prompt+=str(self.lasted[index])+self.unit[index]
        self.begin=0
        self.end=0

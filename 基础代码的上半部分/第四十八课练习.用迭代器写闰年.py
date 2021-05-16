#class LeapYear:
 #   def __init__(self,n=2020):
  #      self.n=n
   #     self.a=0
    #    self.y=0
#    def __iter__(self):
 #       return self
  #  def __next__(self):
   #     self.y=(self.n%4==0 and self.n%100 !=0) or (self.n%400==0)
    #    if self.y>self.n:
     #       raise StopIteration
      #  return self.y
import datetime as dt
class LeapYear:
    def __init__(self):
        self.now =dt.date.today().year#取出当前的年份
    def isLeapYear(self,year):
        if (year%4==0 and year%100 !=0) or (year%100 ==0):
            return True
        else:
            return False
    def __iter__(self):
        return self#变成迭代对象
    def __next__(self):
        while not self.isLeapYear(self.now):#调用自身的isLeapYear
            self.now-=1#若不满足闰年，就-1
        temp=self.now#满足闰年并把当前时间赋值temp
        self.now -=1#当前年份-1
        return temp

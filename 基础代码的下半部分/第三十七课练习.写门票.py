#class Money():
#    usual=100
 #   holiday=usual*1.2
#    spend=0
#    spends=0
#    def child(self):
#        day=int(input("请输入星期几（1,2,3,4,5,6,7）"))
#        if day>0 and day<6:
#            spend=usual/2
#        else:
 #           spend=holiday/2
#            return sepend
 #   def man(self):
#        day=int(input("请输入星期几（1,2,3,4,5,6,7）"))
 #       if day>0 and day<6:
#            spends=usual
#        else:
#            spends=holiday
#            return spends
#    A=spends*2+spend
#    print(A)
class Ticket():#定义类
    def __init__(self,weekend=False,child=False):
        #使用双划线在属性和名字前后，这样外部是访问不到的
        #__init__在类实例化时被自动调用
        self.exp=100
        if weekend:
            self.inc=1.2
        else:
            self.inc=1
        if child:#这里如果child为真，则进行下面函数
            self.discount=0.5
        else:
            self.discount=1
    def calcPrice(self,num):
        return self.exp*self.inc*self.discount*num
    
adult=Ticket()#这里的adult相当于对象
child=Ticket(child=True)
print("2个成人+1个小孩的平日票价为:%.2f"%(adult.calcPrice(2)+child.calcPrice(1)))

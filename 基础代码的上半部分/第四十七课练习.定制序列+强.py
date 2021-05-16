
#class Countlist:
#    def __init__(self,*args):#*args当传入的参数个数未知，且不需要知道参数名称时
 #       self.values=[x for x in args]#让self.values=[args]
  #      index=0
   #     self.count={}.fromkeys(range(len(self.values)),index)
        #dict.fromkeys用于创建一个新字典(seq[, value])
        #seq是字典中的键，value是键对应的初始值
   # def __len__(self):
    #    return len(self.values)
   # def __getitem__(self,key):#当获取容器中制定元素的行为
    #    self.count[key]+=1
     #   return self.values[key]
 #   def __delitem__(self,key):
  #      del self.count[key]
   #     print('%s'% self.count)
class Countlist(list):
    #要求：
    #1.实现获取设置删除一个元素的行为(删除一个元素的时候对应的计时器也会被删除)
    #2.增加counter(index)方法，返回index参数所指定的元素记录和访问次数
    #3.实现append().pop(),remove(),insert(),clear().reverse()方法(重写这些方法的时候主义计数器的改变)
    def __init__(self,*args):
        super().__init__(args)
        self.count=[]
        for i in args:
            self.count.append(0)
    def __len__(self):
        return len(self.count)
    def __getitem__(self,key):
        self.count[key]+=1
        return super().__getitem__(key)
    def __setitem__(self,key,value):
        self.count[key]+=1
        super().__setitem__(key,value)
    def __delitem__(self,key):#删除
        del self.count[key]
        super().__delitem__(key)
    def counter(self,key):
        return self.count[key]
    def append(self,value):#以下的方法作用于列表
        self.count.append(0)
        super().append(value)
    def pop(self,key=-1):
        del self.count[key]
        return super().pop(key)
    def remove(self,value):
        key=super().index(value)
        del self.count[key]
        super().remove(value)
    def insert(self,key,value):
        self.count.insert(key,0)
        super().insert(key,value)
    def clear(self):
        self.count.clear()
        super().clear()
    def reverse(self):
        self.count.reverse()
        super().reverse()

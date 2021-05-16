#class LEn:
 #   i=0
  #  getitme=0
   # def __len__(self):
    #    i+=1
#    def __getitme__(self,key,value):
 #       getitme+=1
  #      print('len  被调用%s次,get被调用%s次'%(i,getitme))

class Countlist:
    def __init__(self,*args):#*args当传入的参数个数未知，且不需要知道参数名称时
        self.values=[x for x in args]#让self.values=[args]
        self.count={}.fromkeys(range(len(self.values)),0)
        #dict.fromkeys用于创建一个新字典(seq[, value])
        #seq是字典中的键，value是键对应的初始值
    def __len__(self):
        return len(self.values)
    def __getitem__(self,key):#当获取容器中制定元素的行为
        self.count[key]+=1
        return self.values[key]

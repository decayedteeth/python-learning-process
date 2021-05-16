import os
import pickle#序列化对象
class MyDes:
    saved=[]
    def __init__(self,name=None):
        self.name=name#名字为
        self.filename=self.name +'.pkl'#将文件名的后缀设置为pkl
    def __get__(self,instance,owner):
        if self.name not in MyDes.saved:#
            raise AttributeError("%s 属性没有赋值" %self.name)

        with open(self.filename,'rb') as f:
            value =pickle.load(f)
        return value
    def __set__(self,instance,value):#当有属性被设立的时候
        with open(self.filename,'wb') as f:
            pickle.dump(value,f)#序列化对象，并将结果数据流入写入到文件中
            MyDes.saved.append(self.name)#saved里面加入属性名
    def __delete__(self,instance):
        os.remove(self,filename)
        MyDes.saved.remove(self.name)

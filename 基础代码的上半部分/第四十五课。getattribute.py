class C:
    def __getattribute__(self,name):#当类的属性被调用是出现，无论是否存在
        print("getattribute")#优先于一切调用
        return super().__getattibute__(name)
    def __getattr__(self,name):#当用户调用一个不存在的属性就会出现
        print("getattr")
    def __setattr__(self,name,value):
        print('setattr')#当一个属性被设置的行为
        super().__setattr__(self,name,value)
    def __delattr__(str,name):#当一个属性被删除时的行为
        print('delattr')
        super().__delattr__(name)

class A():
    def __init__(self):
        print("进入A")
        print("离开A")

class B(A):
    def __init__(self):
        print("进入B")
        super().__init__()
        print("离开B")
        #super会自动找出所有子类盒和对应方法，并且把父系所有重复的地方给删除
class C(A):
    def __init__(self):
        print("进入C")
        super().__init__()
        print("离开C")

class D(B,C):
    def __init__(self):
        
        print("进入D")
        super().__init__()
        #super().__init__(self)
        #这里如果加了self会说你给了两个self，将会报错
        print("离开D")

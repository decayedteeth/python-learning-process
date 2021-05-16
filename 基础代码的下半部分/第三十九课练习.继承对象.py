class Turtle:
    def __init__(self,x):
        self.num = x
class Bird:
    def __init__(self,y):
        self.num = x
class Pool:
    def __init__(self,z):
        self.num = x
class Sky:
    def __init__(self,x,y,z):
        self.turtle=Turtle(x)
        self.fish=Bird(y)
        self.pool=Pool(z)
    def print_num(self):
        print("地上有%d只乌龟，天上有%d只鸟，地上有%d只甲鱼"%(self.turtle.num,self.fish.num,self.pool.num))
        
sky=Sky(1,1,5)
sky.print_num()

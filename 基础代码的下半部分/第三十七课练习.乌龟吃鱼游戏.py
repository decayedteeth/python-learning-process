import random as r
legal_x = [0,10]#这里的legal_x是一个1到10的列表
legal_y = [0,10]
class Turtle:#Turtle英文是乌龟的意思
    def __init__(self):
        self.power = 100
        #初始的体力
        self.x = r.randint(legal_x[0],legal_x[1])#出生在X0到1中
        self.y = r.randint(legal_y[0],legal_y[1])
        #出生位置随机
    def move(self):
        #随机计算方向并移动到新的位置(x,y)
        new_x = self.x + r.choice([1,2,-1,-2])
        new_y = self.y + r.choice([1,2,-1,-2])
        #移动之后是否出X边界
        if new_x < legal_x[0]:
            self.x = legal_x[0]- (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        #检查移动后是否出Y边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        self.power -=1    
        return (self.x,self.y)

    def eat(self):
        #吃掉小鱼后，加生命值
        self.power += 20
        if self.power > 100:
            #若生命值大于100则当100来算
            self.power = 100
class Fish:
    def __init__(self):
        self.y = r.randint(legal_y[0],legal_y[1])
        self.x = r.randint(legal_x[0],legal_x[1])
    def move(self):
        #随机计算方向并移动到新的位置(x,y)
        new_y = self.y + r.choice([1,-1])
        new_x = self.x + r.choice([1,-1])
        #移动之后是否出X边界
        if new_x < legal_x[0]:
            self.x = legal_x[0]- (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        #检查移动后是否出Y边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y   
        return (self.x,self.y)
turtle=Turtle()
fish=[]
for i in range(10):#生成10条鱼
    new_fish = Fish()
    fish.append(new_fish)

while 1:
    if not len(fish):
        print("鱼儿都吃完了,游戏结束")
        break
    if not turtle.power:
        print("乌龟体力耗尽,败北")
        break
    pos = turtle.move()
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼儿被吃掉了...")
all_fish=10-len(fish)
print("一共吃掉了%d条鱼"%all_fish)
    
            

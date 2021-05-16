#类对象和实例对象
class Person(object):
    def __init__(self):
        pass
p1=Person()
print(p1)
#这里的Person是类对象，而p1是实例对象
class OOO(object):
    name="xxx"#类属性
    age =20   #类属性
    def __init__(self):
        self.addr="China" #实例属性

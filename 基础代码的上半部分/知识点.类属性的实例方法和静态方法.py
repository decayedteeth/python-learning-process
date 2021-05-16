class Book(object):#类名
    age =20 #类属性

    def __init__(self,title,name="a"):
        self.title=title  #实例属性
        self.name=name

    @classmethod
    def create(cls,title,x):
        book=cls(title=title,name=x)
        return book#类方法
    @staticmethod#@staticmethod只修饰这个是静态方法
    def cx(x):
        return x#静态方法
    def add(self):
        print(self.title,self.name)
    def lei(self):
        print(self.__class__.age)#实例访问类变量
    @classmethod
    def lei2(cls):
        print(cls.age)#类方法访问变量

book=Book("龙王传说")#实例对象
book.add()#实例方法
Book("龙王传说").add()#类方法
book.title="斗罗大陆"#改变实例属性
book.add()
book.lei2()#访问类方法
print(Book.age)#实例访问类属性
#self和cls的区别不是强制的,self通常用作实例方法的第一参数
#，cls通常用作类方法的第一参数。
#self来传递当前类对象的实例，cls传递当前类对象。

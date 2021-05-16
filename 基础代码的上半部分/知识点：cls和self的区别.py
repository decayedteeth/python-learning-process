class A(object):
    def foo1(self):
        print("Hello",self)
    def foo2():
        print("hello")
    def foo3(cls):
        print("hello",cls)
#self表示一个具体的实例本身
#cls表示类本身
a=A()
a.foo1()
print('最常用的方法，但与下面的方式相同')
A.foo1(a)
print('这里传入实例对象a，相当于普通方法的self')
A.foo2()
print('这里静态方法没有参数，故不可以传东西')
print("这里输入a.foo2或者A.foo2(a)都是错误")


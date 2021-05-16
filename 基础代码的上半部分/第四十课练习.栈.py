class Stack:
    def __init__(self,start=[]):
        self.stack=[]#定义出栈
        for x in start:
            self.push(x)#在栈顶部加入一个数据项

    def isEmpty(self):#判断栈是否为孔
        return not self.stack

    def push(self,obj):#在栈的顶部压入一个数据项
        self.stack.append(obj)

    def pop(self):#pop在栈定出弹出一个数据并删除
        if not self.stack:
            print("栈为空")
        else:
            return self.stack.pop()

    def top(self):#top 显示栈顶部的一个数据
        if not self.stack:
            print('栈为空')
        else:
            return self.stack[-1]

    def bottom(self):#显示栈底的一个数据项
        if not self.stack:
            print('栈为空')
        else:
            return self.stack[0]

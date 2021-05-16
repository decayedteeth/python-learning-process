class Rectangle:
    
    length=5
    width=4
    
    def setRect(self):
        print('请输入长和宽')
        self.length=float(input('请输入长'))
        self.width=float(input('请输入宽'))
    def getRect(self):
        print('你输入的长为%.2f,宽为%.2f'%(self.length,self.width))
    def getArea(self):
        return self.length*self.width
        

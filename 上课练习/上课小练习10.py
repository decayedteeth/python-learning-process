class Person:
    name='人'
    age =30
    def speak(self):
        print("%s 说 我%d岁"%(self.name,self.age))
class Stu(Person):
    def setname(self,newname):
        self.name=newname
    def s_speak(self):
        print("%s 说我%d岁" %(self.name,self.age))
student=Stu()
print('名字是%s',student.name)
print('年龄是%d',student.age)
student.setname('Lily')
student.speak()

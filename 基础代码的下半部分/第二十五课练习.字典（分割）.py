data="1000,小甲鱼,男"
MyDict={}
(MyDict['id'],MyDict['name'],MyDict['sex'])=data.split(',')
#split(sep=NONE,maxspilt=1)默认以空格切换字符串，如果maxspilt有设
#置，则分割maxspilt个字符串
print("ID:   "+MyDict['id'])
print("Name: "+MyDict['name'])
print("Sex:  "+MyDict['sex'])

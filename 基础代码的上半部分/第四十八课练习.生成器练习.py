#def myRev(self,str):
 #   self.str=str
  #  while True:
   #     yield self.str
def myRev(data):
    for index in range(len(data)-1,-1,-1):
        #这里的range是生成data的倒叙索引
        yield data[index]

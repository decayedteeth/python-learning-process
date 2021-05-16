class Nstr(str):
    def __sub__(self,other):
        return self.replace(other,'')
    #str.replace(old,new[,max])是把字符串的old替换成new
    #max是替换的次数不能超过max次
        

class C2F(str):
    def __new__(cls,flaot):
        flaot=flaot*1.8+32
        return str.__new__(cls,flaot)
#class C2F(flaot):
 #   def __new__(cls,arg=0.0):
#        return flaot.__new__(cls,arg*1.8+32)

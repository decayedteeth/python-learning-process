class C:
    @staticmethod
    def static(arg1,arg2,arg3):
        print(arg1,arg2,arg3,arg1+arg2+arg3)
    def nostatic(self):
        print("I m THE normal method")

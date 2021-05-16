class MyRev:
    def __init__(self,data):
        self.data=data
        self.index =len (data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index =0:
            raise StopIteration#raise当执行到错误时候跳过
        self.index=index.index-1
        return self.data[self.index]

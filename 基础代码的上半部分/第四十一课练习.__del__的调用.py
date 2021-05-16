class FileObject:
    def __init__(self,filename='sample.txt'):
        #以读写的模式打开一个文件
        self.new_file = open(filename,'r+')
    def __del__(self):
        self.new_file.close()
        del self.new_file

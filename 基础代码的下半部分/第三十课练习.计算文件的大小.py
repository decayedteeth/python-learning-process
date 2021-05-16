import os#import是模块,模块是一个包含你定义函数和变量的文件，后缀是.py
all_files=os.listdir(os.curdir)
file_dict=dict()
for each_file in all_files:
    if os.path.isfile(each_file):#判断each_file制定路径是否在同一个文件
        file_size = os.path.getsize(each_file)#getsize返回制定文件的尺寸,单位是字节
        file_dict[each_file]=file_size#把每个文件的大小加入字典当中

for each in file_dict.items():#items函数以表的形式返回
    print('%s[%dBytes]'%(each[0],each[1]))

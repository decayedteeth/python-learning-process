import os
all_files=os.listdir(os.curdir)#os.curdir指的是当前目录
#这里是列举当前目录的所有文件
type_dict=dict()#dict用于创建字典
for each_file in all_files:
    if os.path.isdir(each_file):#'os.path.isdir'判断对象是否在且是一个目录
        type_dict.setdefault('文件夹',0)#default若键不在字典中，
        #则添加建返回默认值
        type_dict['文件夹']+=1#这里判断有几个文件夹
    else:
        ext=os.path.splitext(each_file)[1]#splitext分离文件名和扩展名
        #并且ext取后缀
        type_dict.setdefault(ext,0)
        type_dict[ext]+=1#若后缀在里面则+1

for each_type in type_dict.keys():#keys返回一个字典所有的键
    print('该文件夹下工头类型为[%s]的文件%d个'%(each_type,type_dict[each_type]))

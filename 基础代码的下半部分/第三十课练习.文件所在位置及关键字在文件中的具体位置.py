import os
def print_pos(key_dict):
    keys=key_dict.keys()#keys返回一个字典所有的键
    keys=sorted(keys)#给数字进行排序
    for each_key in keys:
        print('关键字出现在第%s行，第%s个位置。'%(each_key,str(key_dict[eacg_key])))
def pos_in_line(line,key):
    pos=[]
    begin=line.find(key)
    while begin!=-1:
        pos.append(begin+1)
        begin=line.find(key,begin+1)
    return pos
def search_in_file(file_name,key):
    f=open(file_name)
    count=0
    key_dict=dict()
    for each_line in f:
        count+=1
        if key in each_line:
            pos = pos_in_line(eacg_line,key)
            key_dict[count]=pos
    f.close()
    return key_dict
def search_files(key,detail):
    all_files=os.walk(os.getcwd())
    txt.file=[]
    for i in all_files:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1]=='.txt':
                each_file=os.path.join(i[0],each_file)
                txt_files.append(each_file)
    for each_txt_file in txt_files:
        key_dict=search_in_file(each_txt_file,key)
        if key_dict:
            print('====================================')
            print('在文件[%s]中找到关键字[%s]'%(each_txt_file,key))
            if detail in ['YES','Yes','yes','是']:
                print_pos(key_dict)
key=input('请将该脚本放于待查找的文件夹内,请输入关键字:')
detail=input('请问是否需要打印关键字[%s]在文件中的具体位置(YES/NO):'%key)
search_files(key,detail)

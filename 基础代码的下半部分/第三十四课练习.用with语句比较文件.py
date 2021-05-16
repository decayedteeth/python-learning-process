def file_compare(file1,file2):
    with open(file1) as f1,open(file2) as f2:
        count=0#统计行数
        differ=[]

        for line1 in f1:
            line2 =f2.readline()#readline每次读出一行内容
            count +=1 #行数+1
            if line1 != line2:#若第一行不等于第二行
                differ.append(count)#在differ列表里面加入不同的行数

        return differ

file1=input('请输入需要比较的头一个文件名:')
file2=input('请输入需要比较的头一个文件名:')

differ = file_compare(file1,file2)
if len(differ)==0:#若differ列表长度为0
    print('两个文件完全一样！')
else:
    print('两个文件共有[%d]处不同'% len(differ))
    for each in differ:
        print('第%d行不一样'% each)#each是指的是之前differ列表加入的不同行数

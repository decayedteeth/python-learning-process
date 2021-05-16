str1='''拷贝过来的字符串'''#三对单,双引号的用法是定义的时候可以定义多行字符串
list1=[]
for each in str1:
    if each not in list1:
        if each =='\n':
            print('\\n',str1.count(each))#'count()'用于统计字符串某个字符出
            #现的个数，可以选择字符串搜索的开始和结束
        else:
            print(each,str1.count(each))
        list1.append(each)#.append 用于在列表末尾添加新的元素

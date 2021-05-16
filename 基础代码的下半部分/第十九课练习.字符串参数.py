def count(*param):
    length = len(param)
    for i in range (length):
        letters=0
        space=0
        digit=0
        others=0
        for each in range[i]:
            if each.isalpha():#若字符串中含有至少一个字母
                letters += 1
            elif each.isdigit():#若字符串中包含数字返回True
                digit += 1
            elif each ==' ':
                space += 1
            else :
                others += 1
        print('第%d 个字符串共有:字母%d个，空格%d个，其他字符%d个。'%(i+1,
              letters,digit,space,others))
count('i love fish .com','cccc    aaaa')

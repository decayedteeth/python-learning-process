str1='''拷贝过来的字符串'''
countA=0
countB=0
countC=0
length=len(str1)
for i in range(length):
    if str1[i]=='\n':
        continue#continue是不执行下面语句 break是终止循环
    if str1[i].isupper():#.isupper()至少包含一个大写的字母 返回Ture
        if countB==1:
            countC+=1
            countA=0
        else:
            countA+=1
        continue
    if str1[i].islower() and countA ==3:#若所有字符串都是小写返回Ture
        countB=1
        countA=0
        target=i
        continue
    if str1[i].islower() and countC==3:
        print(str1[target],end=' ')
    countA=0
    countB=0
    countC=0

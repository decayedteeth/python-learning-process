string = input('请输入一句话:')
def palindrome(string):
    length=len(string) #把len(string)的长度赋值到length上去
    last = length -1#找到最后的元素
    length//=2 #'//'是整除
    flag =1
    for each in range(length):
        if string[each] != string[last]:
            flag=0#把前面的与后面的进行比较，若不相同则flag=0
        last -=1#将最后的last向前推一位

    if flag ==1:
        return 1
    else :
        return 0


if palindrome(string)==1:
    print('是回文联')
else:
    print('不是回文联')


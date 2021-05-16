dec = int(input('输入一个数'))
def Dec2Bin(dec):
    result=''

    if dec:#递归：1.有调用自身 2.有一个正确的返回条件
        result=Dec2Bin(dec//2) #result=dec整除2
        return result + str(dec%2)
    else:
        return result

print(Dec2Bin(dec))

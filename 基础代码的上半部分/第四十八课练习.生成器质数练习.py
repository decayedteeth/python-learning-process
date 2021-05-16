import math#导入数学模块
def is_prime(number):
    if number >1:
        if number==2:
            return True
        if number%2==0:#若能被2整除就不是素数
            return False
        for current in range(3,int(math.sqrt(number)+1),2):
            #range(start, stop[, step])
            #sqrt() 方法返回数字的平方根
            if number % current ==0:
                return False
        return True
    return False
def get_primes(number):
    while True:
        if is_prime(number):
            yield number#把is_prime的素数变成生成器
        number +=1
def solve():
    total =2
    for next_prime in get_primes(3):
        if next_prime < 2000000:#把小于200W的素数
            total += next_prime#加起来
        else:
            print(total)#输出一共的数字
            return
if __name__=='__main__':
    solve()
    

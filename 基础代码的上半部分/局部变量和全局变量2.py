def discounts(price,rate):
    final_price=price*rate
    print('这里试图打印全局变量的值：',old_price)
    return final_price

old_price=float(input('原价是：'))
rate=float(input('请输入折扣:'))
new_price=discounts(old_price,rate)
print('打折后的价格是:',new_price)

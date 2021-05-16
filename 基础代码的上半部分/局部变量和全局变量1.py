def discounts(price,rate):
    final_price=price*rate
    return final_price

old_price=float(input('原价是：'))
rate=float(input('请输入折扣:'))
new_price=discounts(old_price,rate)
print('打折后的价格是:',new_price)
print('这里试图打印局部变量的值：',final_price)
#final-price只在discounts被定义，不能直接拿来用

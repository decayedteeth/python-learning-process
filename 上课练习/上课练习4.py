grade =int(input('请输入成绩'))
if grade >= 90:
    print('优秀')
elif grade>=80:
    print("良好")
elif grade >=70:
    print('中等')
elif grade >= 60:
    print('及格')
elif grade >= 0:
    print('不及格')
else :
    print('输入有误')

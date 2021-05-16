temp=input('输入一个年份')

year=int(temp)
if year/400==int(year/400):
    print(temp+'闰年')
else:
        if (year/4==int(year/4))and(year/100!=int(year/100)):
            print('闰年')
        else:
                print('不是闰年')

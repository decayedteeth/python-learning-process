import xlwt

workbook=xlwt.Workbook(encoding="utf-8")  #创建wookbook对象
worksheet=workbook.add_sheet("sheet1")  #创建工资表
# worksheet.write(0,0,'hello')   #写入数据 第一个是行 第二个是列 第三是内容



for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d= %d"%(i+1,j+1,((i+1)*(j+1))))

workbook.save('student.xls')
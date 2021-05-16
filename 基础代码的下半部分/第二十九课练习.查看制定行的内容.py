def file_view(file_name,line_num):
    if line_num.strip() ==':':#str.strip([chars])‘chars移除制定字符’
        begin='1'#输入格式为n:m则在':'这里进行分割
        end='-1'

    (begin,end)=line_num.split(':')#split在制定分隔符对字符串进行切片

    if begin =='':
        begin='1'
    if end =='':
        end='-1'

    if begin=='1' and end == '-1':#begin=1且end=-1
        prompt='的全文'#输入'1:-1'则会打印全文
    elif begin == '1':#输入'1:n'就会打开相应行数
        prompt='从开始到%s'% end
    elif end == '-1':
        prompt ='从%s到结束'% begin
    else:#若输出的是其他东西
        prompt='从第%s行到第%s行'%(begin,end)
    print('\n文件%s%s的内容如下:\n' %(file_name,prompt))
    begin = int(begin)-1
    end =int(end)
    lines = end - begin
    f= open (file_name)
    for i in range(begin):
        f.readline()
    if lines<0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline(),end='')#每一行输入

        f.close()
file_name=input(r'请输入要打开的文件:')
line_num = input ('请输入需要显示的行数[格式如13:21]')
file_view(file_name,line_num)

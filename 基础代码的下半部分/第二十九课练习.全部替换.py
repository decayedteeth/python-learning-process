def file_replace(file_name,rep_word,new_word):
    f_read=open(file_name)#打开输入的文件

    content=[]
    count=0

    for eachline in f_read:
        if rep_word in eachline:#若所要替换的在里面
            count=eachline.count(rep_word)#count用来计算rep_word出现的次数
            eachline=eachline.replace(rep_word,new_word)#.replace(new,old)把new替换成old
        content.append(eachline)#把替换后的东西放到content里面去

    decide=input('\n文件%s 中共有%s个[%s]\n您确定要把所有的[%s]替换成[%s]吗?\n[YES/NO]:'\
                 %(file_name,count,rep_word,rep_word,new_word))
    if decide in ['YES','Yes','yes','是']:
        f_write = open(file_name,'w')#'w'把原先的文件清空再写入
        f_write.writelines(content)#.write的参数是一个字符串而.writelines的参数是序列,比如列表
        f_write.close()

    f_read.close()
file_name=input('请输入文件名：')
rep_word=input('请输入需要替换的单词或字符：')
new_word =input('请输入新的单词或字符')
file_replace(file_name,rep_word,new_word)

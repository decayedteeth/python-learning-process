print('---欢迎进入通讯录程序---')
print('---1:查询联系人资料---')
print('---2:插入新的联系人---')
print('---3:删除已有联系人---')
print('---4.退出通讯录程序---')

contacts=dict()#此时的contacts相当于一个字典

while 1:#当while 1时候会一直循环
    instr=int(input('\n请输入相关的数字:'))

    if instr==1:
        name =input('请输入联系人名字:')
        if name in contacts:
            print(name+' : '+contacts[name])
        else:
            print('您输入的名字不在通讯录中!')
    if instr == 2:
        name =input('请输入联系人姓名:')
        if name in contacts:
            print('您输入的姓名在通讯录中已经存在-->>',end='')
            print(name +'  :  '+contacts[name])
            if input('是否修改用户资料(YES/NO):')=='YES':
                contacts[name]=input('请输入用户联系电话：')
        else:
             contacts[name]=input('请输入用户联系电话：')
    if instr==3:
        name =input('请输入联系人姓名:')
        if name in contacts:
            del(contacts[name])#也可以使用dict.pop()
#dict.pop(n)用于删除列表中的一个元素,默认为最后一个元素,
#若删除第二个元素则:dict.pop(1)
        else :
            print('您输入的联系人不存在。')

    if instr == 4:
        break#跳出循环

print('---感谢使用通讯录程序---')

import easygui as g
msg ="请填写以下联系方式"
title = "账号中心"
fieldNames=["*用户名","*真实姓名","固定联系电话","*手机号码","QQ","*E-mail"]
fieldValues=[]
fieldValues=g.multenterbox(msg,title,fieldNames)

while 1:
    if fieldValues==None:
        break
    errmsg=""
    for i in range(len(fieldNames)):
        option=fieldNames[i].strip()#strip用于删除开头和结尾的字符，默认删除空格
        #或者换行符,这里是把fieldNames转到option上
        if fieldValues[i].strip()==""and option[0]=="*":
            #这里如果fieldValues和option里面有*
            errmsg+=('[%s]为必填项。\n\n'%fieldNames[i])
            #就在errmsg增加...
    if errmsg=="":
        break
    fieldValues=g.multenterbox(errmsg,title,fieldNames,fieldValues)
print("用户的资料如下:%s"%str(fieldValues))

from bs4 import BeautifulSoup
file=open("作业/总文件.html","rb")
html=file.read().decode("utf-8")
bs=BeautifulSoup(html,"html.parser")

# print(bs.head)
# print(type(bs.head)
# 1.tag 标签及其内容：拿到它所找到的第一个内容



# print(bs.title.string)
# print(type(bs.title.string))
# 2.NavigableString 标签里的内容（字符串）


# print(bs.a.attrs)
# 获取a标签的属性，返回一个字典


# print(type(bs))
# 3.BeautifulSoup  标识整个文档



# print(bs.name)
# 表示整个文档
# print(bs)

# print(bs.a.string)
# print(type(bs.a.string))
# 4.Commet 是一个特殊的NavigableString 输出的内容不包含注释符号

# ---------------------------------------------

# 文档的遍历
# 搜索内容
# print(bs.head.contents)
# print(bs.head.contents[1])


# 文档的搜索

#1..find_all()
#字符串过滤：查找与字符串完全匹配的内容
# t_list=bs.find_all("a")

import re
#(2) 正则表达式:使用search来搜索
# t_list=bs.find_all(re.compile("a"))




#(3) 方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list=bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)

# print(t_list)

#2. kwargs 参数

# t_list=bs.find_all(id="head")
# t_list=bs.find_all(class_=True)
# t_list=bs.find_all(href="http://taobao.com")

#
# for item in t_list:
#     print(item)


# 3.text参数
# t_list=bs.find_all(text="百度")
# t_list=bs.find_all(text=["京东","百度"])

# t_list = bs.find_all(text=re.compile("\d"))
# 应用正则表达式来查找包所含特定文本的内容（标签里的字符串）

# 4.limit 参数
# t_list = bs.find_all("a",limit=3)#limit限制获得的数量
#
# for item in t_list:
#     print(item)


# css选择器
# t_list=bs.select('title')
# 按照标签来查找

# t_list = bs.select(".first")
# 按照类名来查找

# t_list = bs.select("#guangao2")
#通过ID查找

# t_list = bs.select("div[class='left']")
# 通过属性来查找

# t_list = bs.select("body>div>div[id='head']>a")
# 通过子标签查找

t_list=bs.select(".hd3 ~ .bd3")
print(t_list[3].get_text())
# for item in t_list:
#     print(item)
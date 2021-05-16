# 正则表达式

# 字符串模式（判断字符串是否符合一定的标准）

import re
# 创建模式对象

# pat=re.compile("AA")#此处的AA是正则表达式，用来验证其他的字符串
#m=pat.search("CA")#search字符串被校验的内容

# m=pat.search("AABC")
# m=pat.search("AABCDDCCAA")  #search 方法进行比对查找



# 没有模式对象
# m=re.search("asd","Aasd")  #前面的字符串是规则（模板） 后面的字符串是被校验的
# print(m)

# print(re.findall("a","ASDaSDSaaF"))#前面字符串规则（正则表达式），后面字符串是被校验的

# print(re.findall("[A-Z]+","asSDFfsFW"))


#sub

# print(re.sub("a","A","abcdcasd")) #找到a和A替换

# 建议在正则表达式中，被比较的字符串前面加上r 不用担心转义字符串的问题
a=r"\aabd-\'"
print(a)

from bs4 import BeautifulSoup

file= open("2.html","rb")
html=file.read()
bs = BeautifulSoup(html,"html.parser")

# print(bs.a)
# print(type(bs.head))

print(bs.title)
print(bs.title.string)#只拿到标签里面的内容
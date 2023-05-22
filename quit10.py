#89、用两种方法去空格
str="hello world wang hai xia"
a=str.replace(" ","")
print(a)

list=str.split(" ")
b="".join(list)
print(b)
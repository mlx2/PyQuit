#2、如何在一个函数内部修改全局变量

#利用global在函数声明 修改全局变量


a=5
def ma():
    global a
    a=6
ma()
print("a的值是:{}".format(a))
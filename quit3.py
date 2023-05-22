#14、python中生成随机整数、随机小数、0--1之间小数方法

#随机整数：random.randint(a,b),生成区间内的整数

#随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数

#0-1随机小数：random.random(),括号中不传参
import random
import numpy as np
a=random.randint(1,1000)
b=np.random.randn(5)
c=random.random()
print("整数是{}".format(a))

print("小数是{}".format(b))
print("0-1的数是{}".format(c))

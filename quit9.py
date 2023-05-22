#84.递归求和
def ma1(a):
    if a>=1:
        res=a+ma1(a-1)
    else:
        res=0
    return res
res=ma1(10)
print(res)
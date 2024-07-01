#斐波那契数列
def F(x):
    if x == 0:
        return 0
    elif x == 1:
       return 1
    else:
        return F(x - 1) + F(x - 2)

x=int(input("请输入一个数："))
if x<=0:
    print("请输入一个大于0的数")
else:
    liebiao=[]
    for i in range(x):
     liebiao.append(F(i))
    print(liebiao)
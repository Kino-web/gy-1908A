#无参数，无返回值
def fang_fa():
    a = 1
    b = 2
    print(a+b)
fang_fa()
fang_fa()#
#无参数，有返回值
def fang_fo():
    a = 3
    b = 4
    return a+b
c = fang_fo()
print(c)
#有参数，无返回值
def fang_fe(a,b):
    print(a+b)
fang_fe(18526,5445)










#  无参数，无返回值的方法
#   方法定义
def jia_fa():
    a = 1
    b = 2
    print(a + b)
#   方法调用
q = jia_fa()

#  有参数，无返回值的方法
#   方法定义
def jia_fa(a,b):
    print(a+b)
#   方法调用
jia_fa(3,5)
jia_fa(4,10)

#  无参数，有返回值的方法
def jia_fa():
    a = 1
    b = 2
    return a + b

c = jia_fa()
print(c)

#  有参数，有返回值的方法
def jia_fa(a,b):
    return a + b

c = jia_fa(4,7)
print(c)



def mmm(a,b=20):
    return a+b
print(mmm(1))
print(mmm(10,20))
print(mmm(30,b=20))


def nnn(*args,**kwargs):
    print(args)
    print(kwargs)
nnn({"key":"99"},1,2,3,4,5,6,7,x=8,y=9)
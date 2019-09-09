def jia_fa(a,b):
    print(a+b)
jia_fa(1,2)
jia_fa(5,2)

def jia_fa():
    a = 1
    b = 2
    print(a+b)
jia_fa()
#无参数，无返回值
def jia_fa(a,b):
    a = 1
    b = 2
    print(a+b)
jia_fa()
#有参数无返回值
def jia_fa():
    a = 1
    b = 2
    return a+b
c = jia_fa()
print(c)
#有参数，有返回值
def jia_fa(a,b):
    return a+b
c = jia_fa(5,6)
print(c)
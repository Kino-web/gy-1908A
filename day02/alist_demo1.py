l = [1,2,3,4,5,6,7,8,9]
l.append(0)
print(l)

l.insert(4,55)
print(l)

s =[11,22,33]
l.extend(s)
print(l)
print(s)

print(l+s)
print(l)
print(s)

#删除下标删除
print(l.pop(1))
print(l)
print(l.pop())
print(l)
print(l.pop(-3))

#根据内容删除
l.remove(55)
print(l)

#修改列表中数据
l[2]=0
print(l)
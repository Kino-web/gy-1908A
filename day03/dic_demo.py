#增
d = {}
d1 = {'name':'蔡徐坤','sex':'男'}
#新增
d1 ['age'],d1 ['high'] = 18,180
print (d1)
#删除
print(d1.pop('high'))
print(d1)

del d1['age']
print(d1)
#删除整个字典
#del(d1)
#print(d1)
#清空字典
#d1.clear()

#dl = {}


#改
d1['name'] = '吴亦凡'
print(d1)
#字典拼接
#d2 = {'1':123,'2':456}
#d3 = {'4':567,'5':678}
#d2.update(d3)
#print(d2)
#字典合并
d2 = {'1':123,'2':456}
d3 = {'4':567,'5':678}
d4 = dict(d2,**d3)
print(d4)

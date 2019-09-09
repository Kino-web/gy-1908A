for i  in range (1,100,2):
    print(i)
for i  in range (1,100):
    if (i%2==1):
        print(i)
for i in range (100):
    if (i==5):
        break
    print(i)
for i in range (100):
    if (i%3==0):
        continue
    print(i)
a = 0
for i in range(1,101):
    a = a+i
    print(a)

a = 1
for i in range(1,101):
    a =a*i
print(a)

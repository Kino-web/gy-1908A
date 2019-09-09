def ass (a,b):
    try:
        c = a/b
    except:
        print('除数不能为0')
        return
    return c

print(ass(20,0))


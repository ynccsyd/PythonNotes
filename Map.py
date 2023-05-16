def myfunc(a):
    return len(a)

x=map(myfunc, ('py', 'bir', 'programlama', 'dilidir'))
print(x)

# <map object at 0x7f075fbfba00>
# > type(x)
# <class 'map'>
# > list(x)
# [2, 3, 11, 7]

def f(a):
    return a*a 
x=map(f, [1,2,3,4])
print(list(x))
# [1, 4, 9, 16]

# AYnı örnek lambda ile de yapılır
f=lambda a:a*a 
x=map(f, [1,2,3,4])
print(list(x))
# [1, 4, 9, 16]

# Daha kısa yazılımı:
x=map(lambda a:a*a , [1,2,3,4])
print(list(x))

# string listeleri birleştir
f=lambda a,b:a+" "+b
x=map(f,["py","bir"],["proglamlama","dilidir"])
print(list(x))
# ['py proglamlama', 'bir dilidir']

f=lambda a,b:a+" "+b
x=map(f,["py", "bir" ],[ "proglamlama", "dilidir"])
print(' '.join(list(x)))
# py proglamlama bir dilidir
def carp1(a,b):
    return a*b

carp2=lambda a,b:a*b
print(carp1(2,6))
print(carp2(2,6))


#####
f = lambda n: 1 if n == 0 else n * f(n - 1)
f(5)
120
from functools import reduce
f=lambda a1,a2:a1+a2
s=reduce(f,[1,2,3,4])
print(s)
# 10

"""factoriel"""
from functools import reduce
f=lambda a1,a2:a1*a2
s=reduce(f,range(1,5))
print(s)
# 24  =>1*2*3*4
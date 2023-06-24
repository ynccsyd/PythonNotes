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

from functools import reduce
f=lambda a1,a2:a1*a2
s=reduce(f, range(5))
print(s)
#0

from functools import reduce
def tester():
    def reducer(b):
        return reduce(lambda i,j:i+j, b)
    return reducer
x=tester()
print(x(range(5)))
# 10


from functools import reduce
dosya = [1, "ali", "veil", 2, 3, "ayşe", 4]
total = reduce(lambda x, y: x + y, filter(lambda x: isinstance(x, int), dosya))
print(total)

Çıktı:
10

# Reduce kullanarak faktöriyel hesaplayan bir program yazın.
from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

n = int(input("Bir sayı girin: "))  # Kullanıcıdan bir sayı girişi alınır
result = factorial(n) # Faktöriyel hesaplanır
print("Faktöriyel:", result)  # Sonuç ekrana 


from functools import reduce
import random
x= reduce(lambda a,b:a+b, [random.random() for i in range(10)])
print(x)
int(sum(list(map(lambda x,y:x/y,[6,3,5],[2,4,4]))))
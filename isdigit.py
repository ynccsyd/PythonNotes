x=["a",1,"b","c",2,3] 
y=sum([k*2 for k in [i**2 for i in x if str(i).isdigit()]])
print(y)
# 28

from functools import reduce
dosya = [1, "ali", "veli", 2, 3, "ayse", 4]
print(reduce(lambda x, y: x + y, filter(lambda x: isinstance(x, int), dosya)))
# 10
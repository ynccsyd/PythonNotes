
import random 
numbers=[random.random() for i in range(50)]
ek=min(numbers)
eb=max(numbers)
print(ek,eb)




sifreler = ["a123A", "Banana.123", "23dd153", "Apricot", "Orlange"]
x = filter(lambda s: any(c.isupper() for c in s) and any(c.islower() for c in s) and len(s) > 6, sifreler)
print(list(x))
# ['Banana.123', 'Apricot', 'Orlange']


import random

a = set(random.sample(range(1, 50), 6))
b = set(random.sample(range(1, 50), 6))
ortaklar = a.intersection(b)

print("A:", a)
print("B:", b)
print("Ortaklar:", ortaklar)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yuzde = 20
y = list(filter(lambda i: (i > (yuzde + 100) * sum(x) / (len(x) * 100)) or (i < (100 - yuzde) * sum(x) / (len(x) * 100)), x))
print(y)
# [0, 1, 2, 3, 7, 8, 9, 10]

x="python proglamlama dili"
x=x[-6:-18:-5]
print(x)

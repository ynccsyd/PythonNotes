liste=["ali", "veli", "hakan", "suna"]
# Map N girdi alır -N çıktı alır
def map_fonk(a=""):
    return a.capitalize()
buyukler=map(map_fonk, liste)
print(list(buyukler))
# ['Ali', 'Veli', 'Hakan', 'Suna']

# 2nd
y=[i.capitalize() for i in liste]
print(y)
# ['Ali', 'Veli', 'Hakan', 'Suna']

# Filter N girdi - Daha az çıktı
liste=["ali", "veli", "Hakan", "suna"]
def filter_fonk(a=""):
    if a.istitle(): return a
filtre=filter(filter_fonk, liste)
print(list(filtre))
# ['Hakan']

liste=["ali", "veli", "Hakan", "suna"]
def filter_fonk(a=""):
    if a.islower(): return a
filtre=filter(filter_fonk, liste)
print(list(filtre))
# ['ali', 'veli', 'suna']

# Reduce N girdi -1 çıktı
from functools import reduce
liste=["ali", "veli", "Hakan", "suna"]
def reduce_fonk(a="", b=""):
    return a+b
reduce_l=reduce(reduce_fonk, liste)
print(reduce_l)
# aliveliHakansuna

liste=[1,2,3,4,5]
f=lambda a,b:a+b
from functools import reduce
x=reduce(f, liste)
print(x)
# 15
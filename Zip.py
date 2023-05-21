ages=[17,24,99,40]
names=["ali", "veli", "hakan", "suna"]

x=list(zip(names, ages))
print(x)
# [('ali', 17), ('veli', 24), ('hakan', 99), ('suna', 40)]

y=dict(zip(names,ages))
print(y)
# {'ali': 17, 'veli': 24, 'hakan': 99, 'suna': 40}

x=["a", "b","c"]
y=[1,2,3]
z=zip(x,y)
print(dict(z))
# {'a': 1, 'b': 2, 'c': 3}
ages=[17,24,99,40]
names=["ali", "veli", "hakan", "suna"]

x=list(zip(names, ages))
print(x)
# [('ali', 17), ('veli', 24), ('hakan', 99), ('suna', 40)]

y=dict(zip(names,ages))
print(y)
# {'ali': 17, 'veli': 24, 'hakan': 99, 'suna': 40}


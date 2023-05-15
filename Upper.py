cities=["ankara", "roma","london"]
# 1st Best P.
y=[i.upper() for i in cities]
print(y)
# ['ANKARA', 'ROMA', 'LONDON']

# 2nd
for i in range(len(cities)):
    cities[i]=cities[i].upper()
print(cities)
# ['ANKARA', 'ROMA', 'LONDON']
a=["Malatya",1,2,78, "london", "america", "Istanbul",895, "ankara"]

b=[i for i in a  if isinstance(i,int)]
print(b)
# [1, 2, 78, 895]

c=[i for i in a if type(i)==int]
print(c)
# [1, 2, 78, 895]

bb=[i for i in a  if isinstance(i,str)]
print(bb)
# ['Malatya', 'london', 'america', 'Istanbul', 'ankara']

d=[ i if isinstance(i,str) else None for i in a]
print(d)
# ['Malatya', None, None, None, 'london', 'america', 'Istanbul', None, 'ankara']

e=[i for i in a if isinstance(i,str) and i.istitle()]
print(e)
# ['Malatya', 'Istanbul']

"""Divide according to the upper"""
a=["Malatya", "london", "america", "Istanbul", "ankara"]
x=list()
y=list()
[x.append(i) if i.istitle() else y.append(i) for i in a]
print(x)
# ['Malatya', 'Istanbul']
print(y)
# ['london', 'america', 'ankara']

"""with integers"""
a=["Malatya",1,2,78, "london", "america", "Istanbul",895, "ankara"]
x=list()
y=list()
[x.append(i) if isinstance(i,str) and i.istitle() else y.append(i) if isinstance(i,str) else "" for i in a]
print(x)
# ['Malatya', 'Istanbul']
print(y)
# ['london', 'america', 'ankara']


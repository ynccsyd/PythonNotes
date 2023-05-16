x=list(range(10))
print(x)
f=lambda a:a%2==0
s=filter(f,x)
print(list(s))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8]
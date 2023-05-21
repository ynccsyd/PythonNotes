x=list(range(10))
print(x)
f=lambda a:a%2==0
s=filter(f,x)
print(list(s))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8]


sifreler = ["a123A", "Banana.123", "23dd153", "Apricot", "Orlange"]
x = filter(lambda s: any(c.isupper() for c in s) and any(c.islower() for c in s) and len(s) > 6, sifreler)
print(list(x))

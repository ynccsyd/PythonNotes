items=["a","b","c","d","c","b","a"]
s={str(i):items.count(i) for i in items}
print(s)

# {'a': 2, 'b': 2, 'c': 2, 'd': 1}
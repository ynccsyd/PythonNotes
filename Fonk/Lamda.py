def mapScale(factor, nums):
    return map(lambda n: factor * n, nums)

result = list(mapScale(3, [8, 3, 6, 7, 2, 4]))
print(result)

# [24, 9, 18, 21, 6, 12]


def mapPrefixes(string):
    return map(lambda i: string[:i+1], range(len(string)))

result = list(mapPrefixes('cat'))
print(result)
# ['c', 'ca', 'cat']
def isEven(n):
    return n % 2 == 0

result = filter(isEven, [8, 3, 6, 7, 2, 4])
print(list(result))
# [8, 6, 2, 4]

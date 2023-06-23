from functools import reduce

def plus(a, b):
    return a + b

result1 = reduce(plus, [8, 12, 5, 7, 6, 4], 0)
print(result1)  # Output: 42

result2 = reduce(plus, ['I', 'have', 'a', 'dream'], '')
print(result2)  # Output: 'Ihaveadream'

result3 = reduce(plus, [[8, 2, 5], [17], [], [6, 3]], [])
print(result3)  # Output: [8, 2, 5, 17, 6, 3]


# 42
# 'Ihaveadream'
# [8, 2, 5, 17, 6, 3]

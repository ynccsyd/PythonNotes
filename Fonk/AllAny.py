all(map(lambda x: x > 0, [1, 2, -3, -4]))
# Output: False

all(map(lambda x: x > 0, [1, 2, -3, -4]))
# Output: False



any(map(lambda x: x > 0, [1, 2, -3, -4]))
# Output: True

any(map(lambda x: x > 0, [-1, -2, 3, -4]))
# Output: True

any(map(lambda x: x > 0, [-1, -2, -3, -4]))
# Output: False


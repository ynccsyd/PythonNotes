def linesFromFile(filename):
    f = open(filename, 'r')
    lines = map(lambda line: line.strip(), f.readlines())
    f.close()
    return list(lines)

result = linesFromFile('words.txt')
print(result)
# ['ant', 'bat', 'cat']

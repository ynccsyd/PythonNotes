def mapPrefixes(string):
    def prefix(i):
        return string[:i]
    return map(prefix, range(1, len(string) + 1))

print(list(mapPrefixes("python programlama")))

['p', 'py', 'pyt', 'pyth', 'pytho', 'python', 'python ', 
'python p', 'python pr', 'python pro', 'python prog', 
'python progr', 'python progra', 'python program', 'python programl', 
'python programla', 'python programlam', 'python programlama']


def mapPreConcat(pre, strings):
    def concat(i):
        return pre + strings[i]
    return list(map(concat, range(len(strings))))

result = mapPreConcat('com', ['puter', 'pile', 'mute'])
print(result)
# ['computer', 'compile', 'commute']

x=list(range(1,10,2))
y=sum(x[1::2])
print(y)
# 10

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yuzde = 20
y = list(filter(lambda i: (i > (yuzde + 100) * sum(x) / (len(x) * 100)) or (i < (100 - yuzde) * sum(x) / (len(x) * 100)), x))
print(y)
# [0, 1, 2, 3, 7, 8, 9, 10]

kelimeler=("demigod", "madam", "python", "salas" ,"php")
p=list( filter(lambda a: a==a[::-1], kelimeler))
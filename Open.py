def linesFromFile(filename):
    f = open(filename, 'r')
    lines = map(lambda line: line.strip(), f.readlines())
    f.close()
    return list(lines)

result = linesFromFile('words.txt')
print(result)
# ['ant', 'bat', 'cat']



# İçinde alt alta sayılar (hepsi 1-1000 arasında rassal olarak üretilmiş) olduğu varsayılan "sayilar.txt" dosyasındaki sayıları
# okuyarak, en sık geçen sayıyı yazdıran programı kodlayınız. 
f = open("sayilar.txt", "r")
a = f.readlines()
x = {}

for i in a:
    if str(i) in x:
        x[str(i)] += 1
    else:
        x[str(i)] = 1

for k, v in x.items():
    if v == max(x.values()):
        print(k.strip())  # Print the most frequent number without leading or trailing whitespace

f.close()


# 1) Random sayılardan oluşan 10 elemanlı bir liste oluşturarak.
import random
random_list=[random.randint(1,100) for i in range(10)]
    # a. Listenin toplamı, ortalaması
print(random_list)
print("Listenin toplamı:{} , Ortalama:{}".format(sum(random_list),sum(random_list)/len(random_list)))
# [44, 80, 34, 57, 34, 39, 3, 33, 9, 7]
# Listenin toplamı:340 , Ortalama:34.0

    # b. En küçük ve en büyük elemanı
list_max=max(random_list)
list_min=min(random_list)
print(random_list)
print("Max eleman:{} , Min eleman:{}".format(list_max, list_min))
# [44, 92, 46, 75, 60, 51, 52, 70, 100, 77]
# Max eleman:100 , Min eleman:44

    # c. Siralama ve ters siralama
import random
random_list=[random.randint(1,100) for i in range(10)]
random_list.sort()
print(random_list)
random_list.sort(reverse=True)
print(random_list)
# [9, 12, 13, 32, 38, 86, 94, 95, 98, 100]
# [100, 98, 95, 94, 86, 38, 32, 13, 12, 9]

    # d. Liste üzerinde for döngüsü kurma
# 1
import random
random_list=[random.randint(1,100) for i in range(10)]
for i in random_list:
    print(i)
11
38
43
56
8
88
41
36
89
45
# 2. yol
import random
random_list=[random.randint(1,100) for i in range(10)]
for i in range(len(random_list)):
    print(random_list[i]) # print(i, random_list[i]) yaz enumerate olur

        # e. Liste üzerinde enumerate ile döngü kurma
import random
random_list=[random.randint(1,100) for i in range(10)]
for index, value in enumerate(random_list):
    print(index, value)
0 75
1 87
2 6
3 15
4 30
5 35
6 5
7 14
8 31
9 5

        # f. Liste üzerinde azalan sırada enumerate ile indis erişerek döngü kurma
    # g. Listedeki elemanları baştan sona/sondan başa istenilen şartlarda slice yapma

list=[1,2,5,8,7,9,11]
print(list[::-1])
# [11, 9, 7, 8, 5, 2, 1]
list=[1,2,5,8,7,9,11]
print(list[2:4]) #2ve 4 arasındakileri al 4 dahil değil
# [5, 8]
        # h. Pop, append, insert örnekleri yapma
list=[1,2,5,8]
nList=list.pop(2)
print(nList)
list.append(4)
print(list)
# 5
# [1, 2, 8, 4]
"""2) Bir string tanimlayarak"""
"""a.Kelimeyi kariştiran"""
import random
yazi=input("Kelime:")
x=list(yazi)
print(x)
random.shuffle(x)
print(f"Karistirilmis kelime: {x}")
# Kelime:merhaba
# ['m', 'e', 'r', 'h', 'a', 'b', 'a']
# Karıstırılmıs kelime: ['a', 'a', 'm', 'h', 'r', 'b', 'e']

    """b. Rastgele karakter seçen"""
import random
yazi=input("Kelime:")
x=list(yazi)
print(x)
a=random.choice(x)
print(f"rastgele harf: {a}")
# Kelime:merhaba
# ['m', 'e', 'r', 'h', 'a', 'b', 'a']
# rastgele harf: h

    """c. Rastgele n sayida karakter seçen örnekler"""
import random
yazi=input("Kelime:")
x=list(yazi)
print(x)
a=random.sample(x, 3) 
print(f"rastgele harfler: {a}")
# Kelime:merhaba
# ['m', 'e', 'r', 'h', 'a', 'b', 'a']
# rastgele harfler: ['a', 'b', 'r']

"""3) En az bir büyük harf, en az bir küçük harf, en az bir rakam ve 
seçilen özel karakterlerden en az
1 tane içeren, en az 8 harfli bir şifre oluşturma programi kodlayin
"""
import random
uzunluk=4
parola=''
kharfler='abcdefghijklmnoprstuvwyz'
sayilar='0123456789'
ozalkarakter="$,#"

parola+=random.choice(kharfler)
parola+=random.choice(kharfler.upper())
parola+=random.choice(sayilar)
parola+=random.choice(ozalkarakter)

liste=list(kharfler+ sayilar+ kharfler.upper() +ozalkarakter)
for i in range(uzunluk):
    parola+=random.choice(liste)
l=list(parola)
random.shuffle(l)
parola=''.join(l)
print(parola)
# uo5,am$V

"""4) Bir string listedeki tüm kelimeleri capitalize eden bir üretici"""
# 5) Yanlis tasarlanmiş bir veri tabani örneğinde kullanici adlani ve şifrelerinin aşagidaki gibi ayri
# tablolarda yer aldigini varsayarak, tek tabloda olmasi için bir sözlük yapisinda
# {username:password) olacak şekilde birleştirin
# usernames=["ali","veli","ayse","fatma"]
# passwords=["a123", "asdx","1923","f1231."]
# 1 best p
usernames=["all","vell","ayse","fatma"]
passwords=["a123", "asdx","1923","f1231."]
sozluk=dict(zip(usernames, passwords))
print(sozluk)
{'all': 'a123', 'vell': 'asdx', 'ayse': '1923', 'fatma': 'f1231.'
# 2nd
usernames=["all","vell","ayse","fatma"]
passwords=["a123", "asdx","1923","f1231."]
sozluk={}
for i in range(len(usernames)):
    sozluk[usernames[i]]=passwords[i]
print(sozluk)
# {'ali': 'a123', 'veli': 'asdx', 'ayse': '1923', 'fatma': 'f1231.'}

}

"""6) Bir liste üzerinde liste üretici çalistirarak, ortalamadan küçükleri x, büyükleri y listesine atan
üreticiyi kodlayin"""
x=[i for i in range(10)]
k=list()
b=list()
[k.append(i) if i<sum(x)/len(x) else b.append(i) for i in x]
print(k)
print(b)
# [0, 1, 2, 3, 4]
# [5, 6, 7, 8, 9]


import random
x=[random.randint(1,10) for i in range(10)]
k=list()
b=list()
[k.append(i) if i<sum(x)/len(x) else b.append(i) for i in x]
print(x)
print(k)
print(b)
# [5, 8, 5, 8, 8, 8, 7, 6, 2, 6]
# [5, 5, 6, 2, 6]
# [8, 8, 8, 8, 7]

"""sozluk olustr"""
a={str(i):i for i in range(10)}
print(a)
# {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# 1. Lambda kullanarak verilen tamsayılar listesindeki
# her sayının karesini ve küpünü alan python programı:
t_sayilar=[1,2,3,4]
print("Tam sayılar: ",t_sayilar)
karesi=list(map(lambda a:a*a, t_sayilar))
print("Kareleri: ", karesi)
kup=list(map(lambda a:a*a*a, t_sayilar))
print("Küpleri: ", kup)
# Tam sayılar:  [1, 2, 3, 4]
# Kareleri:  [1, 4, 9, 16]
# Küpleri:  [1, 8, 27, 64]

# 2. Math modulü ile çemberin alanını bulma:
import math 
r=int(input("Yaricapi giriniz: "))
alan= math.pi*r*r
print("Yaricapi {} olan cemberin alani {}".format(r, alan))
# Yaricapi giriniz: 2
# Yaricapi 2 olan cemberin alani 12.566370614359172


# 3. Bir diziyi girdi olarak alan ve dizide bulunan büyük ve küçük harflerinden
# sayısını hesaplayan bir python prog. yazın
from functools import reduce
dizi=["bjhLJJJ", "kLLLaa", "AAdddSS", "aaaa","bbbA"]
print(str(dizi))
def reduce_fonk(a="", b=""):
    return a+b
reduce_l=reduce(reduce_fonk, dizi)
print(reduce_l)
kucuk=0
buyuk=0
for i in reduce_l:
    if i.isupper():
        buyuk+=1
    elif i.islower():
        kucuk+=1
print("buyuk harf sayisi:{}, kucuk harf sayisi:{}".format(buyuk,kucuk))
# ['bjhLJJJ', 'kLLLaa', 'AAdddSS', 'aaaa', 'bbbA']
# bjhLJJJkLLLaaAAdddSSaaaabbbA
# buyuk harf sayisi:12, kucuk harf sayisi:16


x=input("yazi giriniz: ")
bharf=sum(map(str.isupper, x))
kharf=sum(map(str.islower, x))
print("buyuk harf sayisi:{}, kucuk harf sayisi:{}".format(bharf,kharf))
# yazi giriniz: şkajbADFVF şljb
# buyuk harf sayisi:5, kucuk harf sayisi:9

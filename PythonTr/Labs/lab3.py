#1. Kullanıcı tarafından girilen yarıçapa göre dairenin alanını hesaplayan kod:
import math
r=int(input("Yariçap giriniz:"))
dAlani=math.pi*r**2
print("{} yarıiçapli dairenin alani: {} olur".format(r,dAlani))
# Yarıçap giriniz:5
# 5 yarıçaplı dairenin alanı: 78.53981633974483 olur


#2. Kullanıcının adını  ve soyadını alan ve aralarıdnda boşluk bırakarak ters 
#sırada yazdıran bir py programı yaz
"""isim:isim
soyisim:soyisim
soyisim isim"""
isim=input("isim giriniz: ")
soyisim=input("soyisim giriniz: ")
print("{} {}".format(soyisim, isim))


#3. (x+y)*(x+y) yi cozmek icin test verisi: x=4, y=3 output=(4+3)^2
x=int(input("x degerini gir:"))
y=int(input("x degerini gir:"))
karesi=(x+y)**2
print("Test verisi x: {}, y:{}".format(x,y))
print("({}+{})^2= {}".format(x,y,karesi))
# x degerini gir:2
# y degerini gir:5
# Test verisi x: 2, y:5
# (2+5)^2= 49


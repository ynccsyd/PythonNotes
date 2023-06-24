class Dairy:
    def karesi(self, pi, r):
        return pi * pow(r, 2)

x = Dairy()
print(x.karesi(3, 2))

###########STATIC
class Dairy:
    @staticmethod
    def karesi(pi, r):
        return pi * pow(r, 2)

print(Dairy.karesi(3, 2))



a = []
b = 0
x = 0

for i in range(8):
    if i % 2 == 0:
        continue
    else:
        a.append(i ** 2)
        b += a[x]
        x += 1

print("Liste uzunluğu:", len(a))
print("x değeri:", x)
print("b değeri:", b)


#  f=1+2+4+16+…+2n toplamını bulan bir programı nesne tabanlı olarak aşağıdaki kurallara göre oluşturunuz (20p).
# a) n sayısı sınıf yapılandırıcı metoduna parametre olarak gönderilecek, f=0 ataması yapılandırıcı içinden yapılacak.
# b) Sınıf değişkeni f'sayısı, sınıfa ait topla isimli metot içinde hesaplanacak ve bu metot yapılandırıcı içinden çağrılacak.
# c) Sınıfin yokedici metodu sınıf değişkeni fsayısını silecek.
class C4:
    def __init__(self, n):
        self.n = n
        self.f = 0
        self.topla()

    def topla(self):
        for i in range(self.n):
            self.f += 2 ** i
        print(self.f)

    def __del__(self):
        del self.f
        del self.n

x = C4(5)
del x

# Bir üstteki sorunun topla metodunu istisna işleme kullanarak yeniden yazın
def topla(self):
    try:
        for i in range(self.n):
            self.f+=2**i
    except:
        print("hata")
    finally:
        print(self.f)


# time: Zamanla ilgili işlemler yapmak için kullanılan bir modüldür. 
#Zamanı ölçmek, beklemek, saat dilimleriyle çalışmak gibi işlemleri gerçekleştirmek 
# için çeşitli fonksiyonlar sağlar.

# random: Rastgele sayılar üretmek için kullanılan bir modüldür. 
# Rastgele sayılar, öğelerin karıştırılması, rastgele seçimler yapılması gibi 
# işlemleri kolayca gerçekleştirmek için çeşitli fonksiyonlar ve sınıflar sağlar.

# sys: Sistemle ilgili işlemler yapmak için kullanılan bir modüldür. 
# Komut satırı argümanlarına erişmek, çıkış yapmak, hata mesajlarını yönetmek, 
# Python yorumlayıcısının çeşitli özelliklerine erişmek gibi işlemleri sağlayan fonksiyonlar 
# ve değişkenler içerir.

# os: İşletim sistemiyle etkileşimde bulunmak için kullanılan bir modüldür. 
# Dosya ve dizin işlemleri yapmak, işletim sistemi fonksiyonlarını çağırmak, sistemle ilgili 
# bilgileri almak gibi işlemleri gerçekleştirmek için çeşitli fonksiyonlar ve değişkenler sağlar.

# math: Matematiksel işlemler yapmak için kullanılan bir modüldür. Trigonometri fonksiyonları, 
# logaritmalar, üstel fonksiyonlar, sayı yuvarlama, faktöriyel gibi matematiksel işlemleri kolayca 
# gerçekleştirmek için çeşitli fonksiyonlar ve sabitler içerir.
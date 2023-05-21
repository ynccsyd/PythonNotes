"""Map, filter, reduce, lambda, iter aliştirmalar"""
# meyveler= “elma armut karpuz ahududu ”
# 1) Yukarıdaki stringten A ile başlayanları filtreleyen tek satırlık kodu yazınız.
meyveler= “elma armut karpuz ahududu ”
y=[i for i in meyveler.split() if i[0]=='a' in i]
print(y) #['armut', 'ahududu']

# 2) Yukarıda stringteki her kelimenin ilk harfini büyük yapan map tek satırlık kodu yazınız.
y=[i.capitalize() for i in meyveler]
print(y)

3) Yukarıdaki örnekleri lambda kullanarak tekrarlayınız.
4) Random üretilen sayıların toplamını reduce kullanarak hesaplatın.
import random
from functools import reduce

sayilar = [random.randint(1, 100) for _ in range(10)]

toplam = reduce(lambda x, y: x + y, sayilar)
print("Toplam:", toplam)

# 5) Aşağıdaki listeden palindroom (tersten okunuşları ile aynı olan) filtreleyen tek satırlık kodu yazınız.
# myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")

myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")
palindromes = list(filter(lambda s: s == s[::-1], myStrings))
print(palindromes)


6) Aşağıda kişilerin fatura tutarları ve son ödeme tarihlerinin yazıldığı bir veri yapısı bulunmaktadır. Son ödeme tarihi geçmiş olanlara %20 gecikme zammı uygulayarak, bir başka sözlüğe borçluları ve borçları aşağıdaki gibi ekleyen kodu yazınız.
Not: çözümde datetime kütüphanesi, map ve list comprehension kullanılarak çıktıyı üreten kod tek satır olarak yazılmıştır.

from datetime import datetime
data = {
    'Ahmet': (200, '2023-05-15'),
    'Mehmet': (150, '2023-05-20'),
    'Ayşe': (300, '2023-05-12'),
    'Fatma': (250, '2023-05-25')
}

borclular = {k: v[0] + v[0] * 0.2 if datetime.strptime(v[1], '%Y-%m-%d').date() < datetime.now().date() else v[0] for k, v in data.items()}
print(borclular)

7) Fibonacci sayılarını hesaplayan sonlu ya da sonsuz bir sınıf yazın.
class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_num = self.curr
        self.prev, self.curr = self.curr, self.prev + self.curr
        return fib_num

8) Reduce kullanarak faktöriyel hesaplayan bir program yazın.

from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

# Kullanıcıdan bir sayı girişi alınır
n = int(input("Bir sayı girin: "))

# Faktöriyel hesaplanır
result = factorial(n)

# Sonuç ekrana yazdırılır
print("Faktöriyel:", result)

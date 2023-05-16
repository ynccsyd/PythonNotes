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
5) Aşağıdaki listeden palindroom (tersten okunuşları ile aynı olan) filtreleyen tek satırlık kodu yazınız.
myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")
6) Aşağıda kişilerin fatura tutarları ve son ödeme tarihlerinin yazıldığı bir veri yapısı bulunmaktadır. Son ödeme tarihi geçmiş olanlara %20 gecikme zammı uygulayarak, bir başka sözlüğe borçluları ve borçları aşağıdaki gibi ekleyen kodu yazınız.
Not: çözümde datetime kütüphanesi, map ve list comprehension kullanılarak çıktıyı üreten kod tek satır olarak yazılmıştır.

7) Fibonacci sayılarını hesaplayan sonlu ya da sonsuz bir sınıf yazın.
8) Reduce kullanarak faktöriyel hesaplayan bir program yazın.
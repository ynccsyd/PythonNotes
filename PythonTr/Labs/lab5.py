# 1. For döngüsü kullanarak br metindeki kelime sayısını bulun
sentence="UML, bir sistemin tasarımını görselleştirmek için yazılım mühendisliği alanında genel amaçlı modelleme dilidir. Yazılı bir dil değildir. Farklı amaçlar için kategorilere ayrılmış olsa da, genel itibariyle modelleme için kullanılır."
sentence=sentence.strip()
sayi=0
for i in sentence:
    if(i== " "): #boşluları sayar bir ekler
        sayi++
print("Kelime sayisi:" str(sayi+1))

# 2nd
sentence="compro un tavolo"
count=len(sentence.split())
print("Kelime sayisi: ", count)
# Kelime sayisi:  3


# 2. Kullanıcı tarafından girilen bir sayının basamaklarının sayı adlarını
# görüntüleyen bir program yazın, örneğin sayı 231 ise çıktısı iki Üç Bir
# olmalıdır.
sayilar={0:"Sifir", 1:"Bir", 2:"iki", 3:"üç", 4:"dört", 5:"beş", 6:"alti", 7:"yedi", 8:"sekiz", 9:"dokuz"}
sayi=input("Tamsayi giriniz: ")
sayi_yazi=""
for i in sayi:
    sayi_yazi+=sayilar[int(i)] + " "
print(sayi_yazi)
# Tamsayi giriniz: 123
# Bir iki üç 

# 2nd
sayilar={
    "0":"Sifir", 
    "1":"Bir",
    "2":"iki",
    "3":"üç", 
    "4":"dört", 
    "5":"beş", 
    "6":"alti", 
    "7":"yedi", 
    "8":"sekiz", 
    "9":"dokuz"}
sayi=input("Tamsayi giriniz: ")

print(*[sayilar[i] for i in sayi])


# 3. List Comprehension yapısı ile daha önceden tanımlanan listedeki
# elemanlarin ilk harflerinden yeni bir liste olusturunuz.
# liste = [ 'Java', 'Python','C', 'Ruby', 'Phb', 'Haskell','C++','Rerl']
# sonuc=['J', 'P','C','R','P','H','C','P']
liste = [ 'Java', 'Python','C', 'Ruby', 'Phb', 'Haskell','C++','Rerl']
nliste=[i[0] for i in liste]
print(nliste)
# ['J', 'P', 'C', 'R', 'P', 'H', 'C', 'R']
# 2nd
basharf=[]
for i in liste:
    basharf.append(i[0])
print(basharf)
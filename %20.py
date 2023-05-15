# Ortalamadan %20 den daha uzak olanları seçen bir liste üretici yaz

x=[0,1,2,3,4,5,6,7,8,9,10]
yuzde=20
y=[i for i in x if(i>((yuzde+100)*sum(x)) / (len(x)*100) or i<((100-yuzde)*sum(x)) / (len(x)*100) )]
print(y)
#  [0, 1, 2, 3, 7, 8, 9, 10]
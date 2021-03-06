'''
    kullanıcıdan aldığınız değerin asal olup olmadığını kullanıcıya yansıtın.
'''

deger=int(input('sayıyı girin : '))
sonuc=True
if deger==1:
    print("Sayı asal değildir")

for x in range(2,deger):
    if deger % x == 0:
        sonuc=False
        break

if sonuc:
    print("Değer asaldır.")
else:
    print("Değer asal değildir.")
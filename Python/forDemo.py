numbers = [1,3,5,7,9,12,19,21]

# # Sayılar listesindeki sayıların toplamı 3'ün kaç katıdır ?
p=0
for x in numbers:
    p+=x
print(p)
print(p//3)

# # Sayılar listesinin eleman toplamları kaçtır ?
p=0
for x in numbers:
    p+=x
print(p)

# Sayılar listesindeki tek sayıların karelerini alınız.
tek=0
for z in numbers:
    if z%2==1:
        print(z,z**2)



sehirler = ["kocaeli","istanbul","izmir","rize"]
# Şehirlerden hangileri en fazla 5 karakterlidir ?
for i in sehirler:
    if len(i)<=5:
        print(i)


urunler=[
    {"name":"Samsung S6","price":"3000"},
    {"name":"Samsung S7","price":"4000"},
    {"name":"Samsung S8","price":"5000"},
    {"name":"Samsung S9","price":"6000"},
    {"name":"Samsung S10","price":"7000"} ] 

# Ürünlerin fiyat toplamı nedir ?
a=0
for z in urunler:
    a+=int(z["price"])
print("Toplam ",a)

# Ürünlerden fiyatı en fazla 5000 TL olan ürünleri gösteriniz.
for z in urunler:
    if int(z["price"])<=5000:
        print(z["name"])
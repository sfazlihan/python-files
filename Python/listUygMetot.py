names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998, 2000, 1998, 1987]

#Cenk ismini listenin sonuna ekleyiniz
names.append("Cenk")
print(names)


#Sena değerini listenin başına ekleyiniz
names.insert(0,'Sena')
print(names)


#Deniz isminin indeksi nedir
print(names.index("Deniz"))


#Deniz ismini listeden siliniz
names.remove('Deniz')
print(names)


#Ali listenin bir elemanı mıdır?
print(names.index('Ali'))

#Liste elemanlarını ters çevirin
names.reverse()
years.reverse()
print(names)
print(years)


#Liste elemanlarını alfabetik olarak sıralayınız
names.sort()
print(names)


#Years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)


#str='Chevrolet','Dacia' karakter dizisini listeye çeviriniz
dizi='Chevrolet Dacia'.split()
print(dizi)


#years listenin en büyük ve en küçük elenamları nelerdir
print(min(years))
print(max(years))

#years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))


#years listesinin tüm elemanlarını siliniz
years.clear()
print(years)


#Kullanıcıdan alacağınız 3 tane marka bilgisini br listede saklayınız
markalar="".split()

a=input("1.Markayı Giriniz...: ")
markalar.append(a)
b=input("2.Markayı Giriniz...: ")
markalar.append(b)
c=input("3.Markayı Giriniz...: ")
markalar.append(c)
print("Markalarınız : ",markalar)

website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Proglamlama Rehberiniz (40 saat)"

#course karakter sayısı
print(len(course))

#website içinden www karakterlerini alın
print(website[7:10])

#website içinden www karakterlerini alın
print(website[-3:])

#course içinden ilk ve son 15 karakterleri alın
print(course[:15]+course[-15:])

#course içindeki karakterleri tersten yazdırın
print(course[::-1])


name, surname, age, job="Fazlıhan","Selvitopi",17,"Yazılımcı"
#ekrana 'Benim adım Fazlıhan Selvitopi, yaşım 17 ve mesleğim yazılımcı' yazdırın
print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}")


# #'Hello world!' ifadesindeki w'yi W ile değiştirin
m="Hello world!"
print(m[0:6]+"W"+m[7:])

#abc yazısını yanyana 3 defa yazdırın
q="abc "*3
print(q)
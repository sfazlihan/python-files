study={}
print("")
print("")
a=input("1.Öğrenci numarasını giriniz...: ")
b=input("Öğrenci adnını giriniz...: ")
c=input("Öğrenci soyadını giriniz...: ")
d=input("Öğrenci telefonunu giriniz...: ")
study[a]={ 'ad':b,
           'soyad':c,
           'telefon':d }
print("")
print("")
e=input("2. Öğrenci numarasını giriniz...: ")
f=input("Öğrenci adnını giriniz...: ")
g=input("Öğrenci soyadını giriniz...: ")
h=input("Öğrenci telefonunu giriniz...: ")
study[e]={ 'ad':f,
           'soyad':g,
           'telefon':h }
print("")
print("")
i=input("3. Öğrenci numarasını giriniz...: ")
j=input("Öğrenci adnını giriniz...: ")
k=input("Öğrenci soyadını giriniz...: ")
l=input("Öğrenci telefonunu giriniz...: ")
study[i]={ 'ad':j,
           'soyad':k,
           'telefon':l }
print("")
print("")
x=input('Görmek istediğiniz öğrencinin numarasını giriniz..: ')
if x==a:
    print(study[a]['ad'])
    print(study[a]['soyad'])
    print(study[a]['telefon'])
elif x==e:
    print(study[e]['ad'])
    print(study[e]['soyad'])
    print(study[e]['telefon'])
elif x==i:
    print(study[i]['ad'])
    print(study[i]['soyad'])
    print(study[i]['telefon'])
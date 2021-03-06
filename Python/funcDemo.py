#Gönderilen bir kelimeyi belirtilen kez ekranda yazdıran fonksiyonu yazın.

def sorubir(kelime,sayi):
    print(kelime*sayi)

sorubir("Fazlıhan\n",5)


#Kendisine gönderilen sınırsız sayıdaki parametreyi bir listeye gönderen fonksiyonu yazın.

def soruiki(*params):
    liste=[]
    for x in params:
        liste.append(x)
    return liste

result=soruiki(2,5,6,4,"Fazlıhan","Selvitopi")
print(result)

#Gönderilen 2 sayı arsındaki tüm asal sayıları bulup ekrana yazdıran fonksiyonu yazın.

def soruuc(sayi1,sayi2):
    for a in range(sayi1,sayi2+1):
        if 1<a:
            for i in range(2,a):
                if(a%2==0):
                    break
            else:
                print(a)

soruuc(10,30)

print()


#Kendisine gönderilen bir tam sayının tüm tam bölen sayılarını ekrana yazdıran fonksiyonu yazın.

def sorudort(giris):
    for x in range(2,giris):
        if giris%x==0:
            print(x)

sorudort(27)
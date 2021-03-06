#Eksiklikler var

def hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    
    ogrenciAdi=liste[0]
    notlar=liste[1]
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3
    return ogrenciAdi+":"+ortalama

def not_oku():
    with open("notlar.txt",encoding="utf-8") as file:
        for satir in file:
            print(hesapla(satir))



def not_gir():
    with open("notlar.txt","a",encoding="utf-8") as file:
        isim=input("isim soyisim  : ")
        not1=input("1.Not : ")
        not2=input("2.Not : ")
        not3=input("3.Not : ")
        file.write(isim + ":"+ not1+","+not2+","+not3+"\n")

def not_kayit_et():
    notlar.close()

while True:
    islem=input("1 - Notları Oku\n2 - Not Gir\n3 - Notları Kayıt Et\n4 - Çıkış\nİşlem : ")
    if islem =="1":
        not_oku()
    if islem =="2":
        not_gir()
    if islem =="3":
        not_kayit_et()
    if islem =="4":
        break
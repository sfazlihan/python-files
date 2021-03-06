# Bankamatik İşlemleri
# Tam çalışmıyor :/
fazlihanHesap = {
    'isim':'Fazlıhan',
    'hesapNo':123456789,
    'bakiye':5000,
    'ekHesap':3000 }
aliHesap = {
    'isim':'Ali',
    'hesapNo':1234567890,
    'bakiye':4000,
    'ekHesap':2000}

def paraCek():
    cikis=int(input(f"Hoşgeldiniz {fazlihanHesap['isim']} Bey, ne kadar çekmek istersiniz : "))
    if cikis <=  fazlihanHesap["bakiye"]:
        print("İşleminiz Tamamlandı.")
        fazlihanHesap["bakiye"] = fazlihanHesap["bakiye"]-cikis
        print(f"Kalan bakiyeniz : {fazlihanHesap['bakiye']}")
    elif fazlihanHesap['bakiye']+fazlihanHesap['ekHesap']>=cikis:
        a=input("Bakiyeniz yetersiz. Ekhesaptan çekmek istermisiniz 'e,y' ? ")
        if a=='e':
            print("İşleminiz Tamamlandı.")
            fazlihanHesap['bakiye']=fazlihanHesap['bakiye']-fazlihanHesap['bakiye']
            q=cikis-fazlihanHesap['bakiye']
            qq=fazlihanHesap['ekHesap']=fazlihanHesap['ekHesap']-cikis
            print(f"Kalan bakiyeniz : {fazlihanHesap['bakiye']} ve ekhesaptan {fazlihanHesap['ekHesap']} lira çekildi.")
        else:
            print("İşlem başarılı olamadı...")
    else:
        print("Yetersiz bakiye...")
print("Hoşgeldiniz,")
giris=input("Hesap İsminizi Giriniz : \n (fazlihanHesap) ")
if giris=="fazlihanHesap":
    print(f"Hoşgeldiniz Sayın fazlihanHesap['isim'],")
    print("Yapılacak İşlemi Seçiniz...: ")
    islem=input("para çekme \nbakiye kontrol \nhesap no sorgulama...: ")
    if islem == "para çekme":
        paraCek()

"""
liste = ["1","2","5a","10b","abc","10","50"]
# Liste elemanları arasndaki sayısal değerleri bulunuz

import re
try:
    for x in liste:
        if re.search("[a-z]",x) or re.search("[A-Z]",x) or re.search("[#$%&_]",x):
            continue
        else:
            print(x)
except Exception as ex:
    print('Hatalı kod yazdınız... : ',ex)

                                VEYA

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
"""


##############################################################################################


"""Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz,
aksi taktirde hata mesajı yazın.

while True:
    import re
    try:
        sayi=input("Bir sayı girin : ")
        if sayi == "q":
            break
            break
        elif (re.search("[a-z]",sayi)) or (re.search("[\s]",sayi)) or (re.search("[A-Z]",sayi)) or (re.search("[a-z]",sayi)) or (re.search("[!?_+*]",sayi)) or (re.search("[%#/()]",sayi)):
            raise Exception('Lütfen gerçek bir sayı giriniz...')
        else:
            print("Girdiğiniz sayı doğru")
            break
            break
    finally:
        print('bitti')
 

                                VEYA



while True:
    try:
        sayi=input("Sayı : ")
        if sayi=="q":
            break
            break
        result=int(sayi)
        print(f"{sayi} sayısı düzgün")
    except ValueError:
        print("lütfen geçerli bir sayı girin")
        continue
"""  


###########################################################################################



"""Girlen parolada türkçe karater hatası veriniz"""
"""
while True:
    import re
    try:
        tr=input('Şifre giriniz : ')
        if (re.search('[ö,ü,ğ,İ,Ü]',tr)) or (re.search('[Ö,Ğ,ç,Ç,ş]',tr)) or (re.search('[Ş,\s]',tr)):
            raise Exception('Parola türkçe karakter içeremez')
            continue
        else:
            print('Şifre Geçerli')
            break
    finally:
        print("bitti")
"""


################################################################################

"""faktöriyel fonksiyonu oloşturup fonksiyona gelen değer için hata mesajları verin"""

def faktoriyel(o):

    if o <= 0:
        raise ValueError("Sayı negatif")
    
    say=1

    for x in range(1,o+1):
        say *= x
    print(say)
fktryl=int(input("Kaç Faktöriyel : "))
faktoriyel(fktryl)
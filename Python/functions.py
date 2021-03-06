def fonkBir():
    print("Fonksiyon kullanımı 1")

fonkBir()

##################################################################

def fonkİki(sayi1, sayi2, sayi3):
    return sayi1 + sayi2 * sayi3


result=fonkİki(5,5,5)
print(result)

##################################################################

def fonkUc(name = "User"):
    return (f"Hello {name}")

result=fonkUc()


###################################################################

def fonkUyg(isim, dogumTarihi):
    asd=(2020-dogumTarihi)
    return print(f"{isim} , {asd} yaşında !")

result=fonkUyg("Fazlıhan",2003)
print(result)

###################################################################

def myFunc(a,b,c,*d,**e):       # d* derken liste istemiş olduk,
    print(a)                    # e** derken dictionary istemiş olduk.
    print(b)
    print(c)
    print(d)
    print(e)

result=myFunc(10, 20, 30, 40, 50, 60, 70, d1 = "değer1", d2 = "değer2")
print(result)
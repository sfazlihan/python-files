'''
    1-100 arsında rastgele üretilecek bir sayıyı aşağı-yukarı gibi ifadelerle tahmin etmeye çalışın.
    **  100 üzerinden puanlama yapın.
    **  Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzrinden hesaplansın.

'''

import random
sayi=random.randint(0,100)
print("Sayı tahmin oyununa hoşgeldin")
print("   **Oyun 100 üzerinden hesaplaacaktır.")
print("   **0 - 100 arasında bir satı tuttum")
can=int(input("  ***Kaç tahmin hakkı istiyorsunuz = "))
puan= 100/can
for x in range(can):
    x=int(input(" Sayıyı tahmin et bakalım :) "))
    if x == sayi:
        print(f"Tebrikler {sayi} sayısını bildiniz")
        sonuc=puan*can
        print("Puanınız : ",sonuc)
        break
    else:
        can-=1
        print(f"Bilemedin {can} hakkın kaldı")

        if sayi<x:
            print("Daha küçük")
        else:
            print("Daha büyük")
        if can == 0:
            print("Oyun Bitti")
            print(f"Tuttuğum sayı {sayi} idi :)")
# Error Handling => Hata Yönetimi



# try:
#     x=int(input('x : '))
#     y=int(input('y : '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as hata:   # Hata mesajını görebiliriz ve hata takma ismine attık ve şunu dedik :
#     print('Yanlış bilgi girdiniz... ',hata)


# try:
#     x=int(input('x : '))
#     y=int(input('y : '))
#     print(x/y)
# except Exception:       # Her hata türüne karşılık şunu dedik (hata türünü göremeyiz):
#     print('Yanlış bilgi girdiniz... ')

while True:
    try:
        x=int(input('x : '))
        y=int(input('y : '))
        print(x/y)
    except Exception:       # Her hata türüne karşılık şunu dedik (hata türünü göremeyiz):
        print('Yanlış bilgi girdiniz... ')
    else:
        print('İşleminiz sorunsuz tamamlandı.') # Herşey doğruysa bunu yazar ve döngüden çıkar
        break
    finally:                # İşlemler tamamlandığında bunu yapar:
        print('İşlem bitti...')
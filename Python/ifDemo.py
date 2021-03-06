#-------- Kullanıcıdan isim, yaş, eğitim bilgisi isteyip ehliyet alabilme durumunu kontrol ediniz.
#--------Ehliyet alma koşulu en az 18 ve eğitim durumu lise yada üniversite olmalıdır.


isim=input('İsminizi Giriniz : ')
yas=int(input('Yaşınızı Giriniz : '))
durum=input('Eğitim Durumunuzu Giriniz : ')

if (yas>=18 )and (durum=='lise' or 'üniversite'):
    print(isim, ' Bey, Ehliyet Alabilirsiniz :)')
else:
    print(isim,' Bey, ehliyet almak için gerekli özelliklere sahip değilsinz')


#---------------------Bir öğrencinin iki yazılı bir sözlü notunu alıp,
# hesaplanan ortalamaya göre not ağırlığına göre karşılık gelen not bilgisini yazdırınız.
# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5


bir=float(input('1.Yazılı Notunu Giriniz..: '))
iki=float(input('2.Yazılı Notunu Giriniz..: '))
uc=float(input('Sözlü Notunu Giriniz..: '))

ort=(bir+iki+uc)/3

if ort<=24.99:
    print('0')
elif ort>=25 and ort<=44.99:
    print('1')
elif ort>=45 and ort<=54.99:
    print('2')
elif ort>=55 and ort<=69.99:
    print('3')
elif ort>=70 and ort<=84.99:
    print('4')
elif ort>=85:
    print('5')
else:
    print('Hatalı Giriş Yaptınız')


#
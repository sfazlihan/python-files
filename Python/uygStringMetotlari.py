website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Proglamlama Rehberiniz (40 saat)"
print("")
# 1-)   ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterleri silin.
hello=' Hello World '
print(hello.replace(' H','H').replace("d ","d"))
print("")
# 2-)    'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin
w='www.sadikturan.com'
print(w[4:-4])
print("")
# 3-)   course karakter dizisinin tüm karakterlerini küçük harf yapın
print(course.lower())
print("")
# 4-)   course dizisinin içinde kaç tane "a" karakteri var ? (count("a"))
print(course.count('a'))
print("")
# 5-)   website www ile başlayıp com ile bitiyormu
print(website.startswith("www"))
print(website.endswith("com"))
print("")
# 6-)   website içinde .com varmı ?
print(website.find(".com"))
print("")
# 7-)   course içindeki karakterlerim hepsi alfabetikmi ? (isalpha, isdigit)
print(course.isalpha())
print("2112".isdigit())
print("")
# 8-)   'Contents' ifadeini satırda 50 karakter içine yerleştirip sağ ve soluna * koyunuz
print("Contents".center(50,'*'))
print("Contents".ljust(50,'*'))
print("Contents".rjust(50,'*'))
print("")
# 9-)   course dizisindeki tüm boşluk karakterlerini - ile değiştirin
print(course.replace(" ","-"))
print("")
# 10-)  'Hello World' karakter dizisindeki world ifadeinin 'There' olarak değiştirin
h="Hello World"
print(h.replace('Hello','There'))
print("")
# 11-)  'course' karakter dizisini boşluk karakterlerinden ayırın.
print(course.replace(' ',''))
print("")
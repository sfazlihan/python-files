print("")
print("")
message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.upper())
print("upper()   //   Hepsini büyük harfle yazar")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.lower())
print("lower()   //   Hepsini küçük harfle yazar")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.title())
print("title()   //   Her kelimenin ilk harfini büyük yazar")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.capitalize())
print("capitalize()   //   Metnin sadece ilk harfini büyük, diğerlerini küçük yapar")
print("")

message = "  Hello there. My name is Fazlıhan Selvitopi"
print(message.strip())
print("strip()   //   Metnin başında/sonunda boşluk varsa siler")
print("")


message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.split())
print("split()   //   Metnin kelimelerini dizi şeklnde ayırır")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print("".join(message))
print("join()   //   Dizilere ayrılmış metni aralarına boşluk ekleyek birleştirir")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.find("Fazlıhan"))
print("find()   //   Metinde arattağımız kelime veya harf varsa index numarasını, yoksa '-1' değerini verir")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.startswith("Hello"))
print("startswith()   //   Metin girilen karakter/kelime başlıyorsa True, başlamıyorsa False değerini verir")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.endswith("8"))
print("endswith()   //   Metin girilen karakter/kelime bitmiyorsa True, başlamıyorsa False değerini verir")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.replace("Hello","Merhaba"))
print("replace()   //   Metinde ilk girilen değeri aratır, varsa ikinci girilen değer ile değiştirilir")
print("")

message = "Hello there. My name is Fazlıhan Selvitopi"
print(message.center(75))
print("center()   //   Metni girilen değer kadar sağ ve soldan eşit olarak boşluk bırakarak yazar")
print("isteğe göre center(100,'*')  olarakta yazdırılabilir.Bu durumda çıktı :")
print(message.center(75,"*")+"  olarak görülür")
print("")
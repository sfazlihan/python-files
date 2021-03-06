file = open("files1.txt","r",encoding="utf-8")   #  ==    file = open("files1.txt",encoding="utf-8")
# print(file)

"""
# try:
#     file = open("files1.txt","r",encoding="utf-8")
# except FileNotFoundError:
#     print("Dosya açılamadı")
# finally:
#     print('Dosya kapandı.')
#     file.close()


# For döngüsü
for x in file:
    print(x, end="")
file.close()

"""

#read() fonksiyonu

content1=file.read()
print(content1)
"""
content2=file.read()
print(content2) # burada yazmaz çünkü imleç dosyanın sonunda ve dosya kapanmadı.Yeniden dosyayı açmamız gerekir.

file.close()

snc = file.read(5)  #ilk 5 karakterini okur
snc = file.read(3)  #imleçten sonraki 3 karakterini okur
print(snc)

"""

#readline() fonksiyonu,   satır satır yazdrır
"""
print(file.readline())      #satır sonuna boşluk ekler
print(file.readline(), end="")   
print(file.readline())   
print(file.readline())   

"""


#readlines() fonksiyonu,   satırları liste halinde sıralar.
"""
liste=file.readlines()
print(liste)
print(liste[2])
"""

file.close()
# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı :     open("dosya_adi","dosya_erisme_modu")
# dosya_erisme_modu => dosyaya hangi amaçla açtığımızı belirtir

"""
    "w" : yazma modu. Dosyayı konumda oluşturur.
    "a" : ekleme modu. Dosya konumda yoksa oluşturur.
    "x" : oluşturma(creative) modu. Dosya zaten varsa hata verir.
    "r" : okuma modu. Dosya konumda yoksa hata verir.
"""
# "w":

"""result=open("files1.txt","w",encoding="utf-8")
result.write("Fazlıhan Selvitopi")
result.close()
print(result)"""




# "a":

"""result=open("files1.txt","a",encoding="utf-8")
result.write("Fazlıhan Selvitopi\n")
result.close()"""



# "x":

"""result=open("files1.txt","x",encoding="utf-8")
result.close()"""
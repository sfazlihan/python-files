import os
import datetime
# print(dir(os))


#***************IŞLETIM SISTEMI ISMINI VERIR.***************
# result = os.name   


#*****************ETKİN DİZİNİ ÖĞRENME**********************
# result=os.getcwd()


#********************DİZİN DEĞİŞTİRME***********************
# os.chdir("C:\\")
# os.chdir('../..')


#*******************KLASÖR OLUŞTURMA*****************************
# os.mkdir("Yeni Klasor")
# os.makedirs("NewKlasör/yeniii")  # iç içe klasör oluşturma
# os.rename('NewKlasör','yeniKlasor')   #klasör ismini değiştirir.
# os.rmdir("yeniKlasor")   #klasörü alt elemanlarını ile siler.     
# os.removedirs('NewKlasör/yeniii')   #sadece belirtilen klasörü siler

#*************************LİSTELEME*************************
# result=os.listdir()           # bulunduğu klasördeki dosyaları listeler
# result=os.listdir("C:\\")     # C:\\ altındaki dosyaları listeler
# for dosya in os.listdir():
#     if dosya.endswith('.txt'):      # .txt uzantılı dosyaları gösterir.
#         print(dosya)


#*******************DOSYA HAKKINDA BİLGİ ALMAK*******************
# result=os.stat('files.py')      #dizin içindeki dosyadan bilgi alır.
# result=result.st_size/1024      #kaç kB?
# result=datetime.datetime.fromtimestamp(result.st_ctime)   #oluşturulma tarihi
# result=datetime.datetime.fromtimestamp(result.st_atime)   #son erişilme tarihi
# result=datetime.datetime.fromtimestamp(result.st_mtime)   #son düzenlenme tarihi

#********************Belirtilen dosyayı açma********************
# os.system('notepad.exe')
# os.system('calc.exe')


# ______________________________path_______________________________

result=os.path.abspath('atama.py')  #klasörünü gösterir ve:
result=os.path.dirname("C:/Users/İRŞADİ/Desktop/Fazlihan/Python/atama.py")  #Dizinini.gösterir. 
result=os.path.dirname(os.path.abspath("atama.py"))#Aslında bu şekilde kullanılırlar.

result=os.path.exists("C:/Users/İRŞADİ/Desktop/Fazlihan/Python/atama.py")  #bu dosya var mı?
result=os.path.exists("C:/Users/İRŞADİ/Desktop/Fazlihan/Python/atamaa.py")  #bu dosya var mı?
     
result=os.path.isdir("C:/Users/İRŞADİ/Desktop/Fazlihan/Python")     #Bu bir klasör mü?
result=os.path.isfile("C:/Users/İRŞADİ/Desktop/Fazlihan/Python/atama.py")   #Bu bir dosya mı?

result=os.path.join("C:\\","Users")     #Elemanları birleştirip bize yol verir.

result=os.path.split("C:\\deneme")      #Yolu tek tek ayırır.
result=os.path.splitext("atama.py")     #Dosyanın ismini ve uzantısını ayırır


print(result)
print(result[0])
print(result[1])
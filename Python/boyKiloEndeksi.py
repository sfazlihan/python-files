class Deneme:
    def __init__(self,age, health):
        self.age= 2020-b
        self.health=endex



a=input('İsminizi girin...: ')
b=int(input('Doğum tarihinizi girin...: '))
c=int(input('Kilonuzu girin...: '))
d=float(input("Boyunuzu ('örn:1.70')'nokta' cinsinden girin...: "))

endex=c/d**2
if endex < 18.5:
    sonuc='zayıfsın.'
elif endex >= 20 and endex <= 25:
    sonuc='kilona göre normal.' 
elif endex >= 25 and endex <= 30:
    sonuc='şismansın.'
elif endex > 30:
    sonuc='acilen kilo vermen gerek.'


kisi=Deneme(b,endex)
yaz=(f'{a}, {kisi.age} yaşındasın ve <boy/kilo> endeksine göre {sonuc}')
print(yaz.title())
print(kisi)
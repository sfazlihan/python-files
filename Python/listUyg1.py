print("")
theList="Bmw Mercedes Opel Mazda".split()
print("")

#liste kaç elemanlı ?
print(len(theList))
print("")



# Listenin son elemanı
print(theList[-1])
print("")



#mazda değerini toyota ile değiştirin
theList[3]='Toyota'
print(theList)
print("")


#mercedes listenin bir elemanı mıdır ?
print(theList.index('Mercedes'))
print("")



#Listenin -2 nolu indisinde ne vardır ?
print(theList[-2])
print("")



#Listenin ilk 3 elemanını yazdırın
print(theList[0:3])
print("")



#Liste üzerine nissan ve audi ekleyin
a="Nissan","Audi"
theList+=a
print(theList)
print("")



#listenin son 2 elemanı yerine toyota ve renault ekleyin
theList[4]="Toyota"
theList[5]="Renault"
print(theList)
print("")


#listenin son elemanını silin
del theList[5]
print(theList)
print("")



#liste elemanlarını tersten yazdırın
print(theList[::-1])
print("")



studentA="Yiğit Bilgi 2010, (70,60,70)"
print(studentA)
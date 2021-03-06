fruits ={"Cherry","Mango","Apple","Banana"}
print(fruits)
# fruits[2]="Elma"    indexlerine birşey atayamayız.

for x in fruits:
    print(x)

fruits.add("Orange")        #listeye eleman ekledik
fruits.update(["Üzüm","Karpuz","Apple"])    #lsteye elemanlar ekledik ---(olanı birdaha yazmadı)---
print(fruits)


fruits.remove("Cherry")     #eleman çıkardık
fruits.discard("Mango")
print(fruits)

fruits.pop()            #rastgele elenman sildik
print(fruits)

fruits.clear()          #listeyi boşalttık
print(fruits)

myList=[0,0,1,2,2,3,4,4,5]
print(set(myList))      #tekrarlanan elemanları göstermeden yazdırdık
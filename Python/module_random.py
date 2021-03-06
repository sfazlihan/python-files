import random                   #random modülünü

print(dir(random)) # 'random modülünde hangi metotlar var?'


list1=[0,1,2,3,4,5,6,7,8,9]

print(random.sample(list1,4))   #belirtilen listeden belirtilen sayı kadar değer döndürür

print(random.choice(list1))     #belirtilen listeden 1 tane değer döndürür

print(random.randint(0,100))    #belirlenen aralıkta rastgele int sayı döndürür

print(random.randrange(30,51,10))  #belirlenen arakılta rastgele float sayı döndürür(bir parametre daha alır o parametre de bölünebilmeyi ifade eder.)

print(random.random())          #0-1 arasında rastgele değer döndürür

print(random.shuffle(list1))    #belirtilen listenin sırasını karıştırır

print(random.uniform(20,25))    #belirtilen aralıklarda float sayı döndürür

names = ['Cenk','Ayşe','Ali','Feyza','Ahmet']
result = names[random.randint(0,len(names)-1)]
###
result = random.choice(names)

greeting='Hello there'
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
print(liste)

liste=(range(100))
print(random.sample(liste,5))

print(result)















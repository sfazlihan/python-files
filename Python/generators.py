# Generators, işlemleri anlık yapan ve bellekte yer tutmayan işlemler için kullanılır.

def generators():
    liste=[]
    for i in range(5):
        liste.append(i**3)
    print(liste)
generators()
#Bunun yerine:
def generators():
    for i in range(5):
        yield i**3
for i in generators():
    print(i)



liste=[ x**3 for x in range(5) ]    #liste halinde yazdırır.
print(liste)



liste=( x**3 for x in range(5) )    #generators objesini verir.
print(liste)

for i in liste:     #listeyi alt alta yazdırır.
    print(i)
isim = "Fazlıhan"

for x in isim:
    if x == "l":
        continue
    print(x)

print("")

for x in isim:
    if x == "l":
        break
    print(x)


#1 de 100e kadar tek sayıların toplamını alalım
a=0
i=0
while i<=100:
    i+=1
    if i % 2==0:
        continue
    a+=i
print(a)

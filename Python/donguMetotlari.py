#range()
for g in range(10):
    print(g)

for a in range(0,100,25):
    print(a)

#enumerate()
lee='Fazlıhan'
for item in enumerate(lee):
    print(item)

#zip()
liste1=[20,40,60,80,100,120]
liste2=["P","Y","T","H","O","N"]
qwerty=list(zip(liste1,liste2))
print(qwerty)
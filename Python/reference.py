#   VALUE TYPES

a=25
b=75

a=b

b=50            # a'ya etkisi olmadı

print(a)

##################################################

#   REFERENCE TYPES

c=["Mavi","Kırmızı"]
d=["Mavi","Kırmızı"]

c=d

d[0]="Yeşil"        # c'yi etkiledi

print(c,d)
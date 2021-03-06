x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1) Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z nin topplamının farkı kaçtır?
a=int(input("1.Sayıyı Giriniz...: "))
b=int(input("1.Sayıyı Giriniz...: "))
q=(a*b)-(x+y+z)
print('Sonuç..: ',q)

# 2) y'nin x'e kalansız bölümü kaçtır?
print(y//x)

# 3) (x,y,z)nin toplamının mod 3 ü kaçtır?
print((x+y+z)%3)

# 4) y'nin x kuvvetini hesaplayınız.
print(y**x)

# 5) x, *y, z = numbers işlemine göre z'nin küpü kaçtır?
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
print(z**3)

# 6) x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
toplam=0
for c in y:
    toplam+=c
    print(toplam)
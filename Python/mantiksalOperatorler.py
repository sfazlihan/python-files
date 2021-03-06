a, b, c = 5, 10, 47
passsword='karakartal25'

# and           en az 2 seçenek sunar ve 2 si de anlamı katar
resault=(a==5)and(c<100)
resault=(a==5)and(passsword=='karakartal')

# or            en az 2 seçenek sunar yada anlamı katar
resault=(b<15)or(passsword=='karakartal')
resault=(a<5)or(c<100)

#not            en az 2 seçenek sunar,değeri ters çevirir.
resault=not(a==5)
resault=(not(a==5))and(passsword=='karakartal25')



print(resault)
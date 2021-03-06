# ben={
#     'isim' :'Fazlıhan','soyisim' : 'Selvitopi','yaş' : 17}

# print(ben["isim"])        #Ekranda Fazlıhan yazar.


users={
        'Fazlıhan':{
            'surname':'Selvitopi',
            'address':'Tuzla/İSTANBUL',
            'age': 17,
            'email': 'sfazlihan@gmail.com'
        },

        'Ahmet':{
            'surname':'Yıldırım',
            'address':'Pendik/İSTANBUL',
            'age': 17,
            'email': 'ahmet@gmail.com'
        }
}
print(users)
print(users['Fazlıhan']['age'])
print(users['Fazlıhan']['surname'])
print(users['Fazlıhan']['address'])
print(users['Fazlıhan']['email'])
print('')
print(users['Ahmet']['age'])
print(users['Ahmet']['surname'])
print(users['Ahmet']['address'])
print(users['Ahmet']['email'])
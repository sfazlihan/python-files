# #pass Boşluk doldurmaya yarar

#Class
class Person:

    #class attributes
    address='İstanbul'
    pi=3.14
    name='Fazlıhan'
    #constructor (yapıcı metod)
    def __init__(self,name,age):    #self, örnekteki 'a'
    #object attributes
        self.name = name
        self.age = age
        print('init metodu çalıştı.')


    #methods
    def intro(self):
            print('Selam, ben '+ self.name)


#object, instance
a=Person('Fazlıhan',17)
a.intro()
print(f'Name : {a.name}, Age : {a.age}, Address : {a.address}')
# #updating,bilgileri günceller.
# a.age=18


class Hesaplamalar():
    #Class object attribute
    pi=3.14

    def __init__(self, yaricap=1):
        self.yaricap=yaricap

    #Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)



c1=Hesaplamalar() # yarıçap = 1
c2=Hesaplamalar(5)

print(f'c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')

print(c1)
print(c2)
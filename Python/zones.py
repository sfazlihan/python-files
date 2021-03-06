name = "Fazlıhan"           #global zone

def isim():
    name = "Alparslan"      #local zone
    print(name)

print(name)
isim()

###############

name = 'Fazlıhan'

def changeName(new_name):
    name=new_name
    print(name)

print(name)
changeName('Alparslan')

################################################################

name = 'Global String'

def greeting():
    name="Çınar"

    def hello():
        print("hello"+name)

    hello()
greeting()

#################################################################

x=50

def test():
    global x    # global olan x'i kullanmak için 'Global' keyword'ünü çağırdık
    print(f"x to {x}")

    x=100
    print(f"changed x to {x}")
test()
print(x)

##################################################################
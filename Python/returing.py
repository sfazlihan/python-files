"""
def usalma(number):

    def inner(power):
        return  number ** power

    return inner


first=usalma(5)
third=usalma(4)

print(first(5))
print(third(3))
"""
######################################################
"""
def yetki_sorgula(page):

    def inner(role):
        if role =="admin":
            return f"{role} , {page} sayfasına ulaşabilir."
        else:
            return f"{role} , {page} sayfasına ulaşamaz."

    return inner

account1=yetki_sorgula("yazilimolog")
print(account1("admin"))

account2=yetki_sorgula("yazilimolog")
print(account2("user"))
"""
#######################################################
def islem(islem_adi):

    def topla(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam


    def carp(*args):
        _toplam=1
        for i in args:
             _toplam*=i
        return _toplam


    if islem_adi=="toplama":
        return topla
    elif islem_adi=="carpma":
        return carp

islem1=islem("toplama")
print(islem1(4,4,5,7,6,9))

islem2=islem("carpma")
print(islem2(4,4,5,7,6,9))
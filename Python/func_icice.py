def faktoriyel(number):

    if not isinstance(number,int):
        raise ValueError("Gerçek sayı girin.")
    if number <= 0:
        raise Exception("Sayı sıfırdan büyük olmalı")

    def inner_faktoriyel(number):

        if number <=1:
            return 1

        return number * inner_faktoriyel(number-1)
    
    return inner_faktoriyel(number)

try:
    print(faktoriyel(10))
except Exception as ex:
    print(ex)
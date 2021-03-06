"""
def myDecorator(func):
    print("Fonksiyondan önceki işlemler")
    func()
    print("Fonksiyondan sonraki işlemler")

@myDecorator
def sayHello():
    print("Hello")

# sayHello=myDecorator(sayHello)  bunun yerine '@myDecorator'kullanalım.
sayHello
"""




import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print("fonksiyon "+func.__name__+", "+str(finish-start)+" saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(number):
    print(math.factorial(number))

@calculate_time
def topla(a,b):
    print(a+b)

usalma(2,5)
faktoriyel(6)
topla(9,15)
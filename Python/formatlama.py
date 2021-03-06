name="Fazlıhan"
surname="Selvitopi"
age=16

print("My name is {} {} . I am {} years old.".format(name,surname,age))
print("My name is {2} {0} . I am {1} years old.".format(name,surname,age))
print("My name is {n} {s} . I am {a} years old.".format(n=name,s=surname,a=age))

result= 500/700
print("The result is {r:1.4}".format(r=result))
#r önündeki 1 virgülden önceyi, 4 sonraki rakam sayısını temsil eder.

print(f"My name is {name} {surname} . I am {age} years old.")                                             
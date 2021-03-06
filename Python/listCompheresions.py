###############################################################
numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)

number=[ x for x in range(10)]
print(number)

###############################################################

for x in range(10):
    print(x**2)

for2 = [ x**2 for x in range(10)]
print(for2)

################################################################

myString = 'Hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

################################################################

years=[2000,1934,1978,2003,1993]
ages=[ 2020-x for x in years ]
print(ages)

################################################################

result=[ x if x%2==0 else 'TEK' for x in range(1,10) ]
print(result)

################################################################

forr=[]
for x in range(3):
    for y in range(3):
        forr.append((x,y))
print(forr)

add = [ (x,y) for x in range(3) for y in range(3) ]
print(add)

#################################################################
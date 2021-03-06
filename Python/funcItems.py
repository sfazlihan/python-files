def square(num): return num**2
result=square(5)
print(result)

###############################################

liste=[1,3,5,7,9]
result=list(map(square,liste))
print(result)

###############################################

liste=[1,3,5,7,9]
result=list(map(lambda num : num**2,liste))
print(result)

###############################################

for item in map(square,liste):
    print(item)

###############################################

def check_even(num) : return num % 2 == 0 

liste=[1,3,5,7,9,10,8,16,1,11,18]
print(list(filter(check_even,liste)))
x,y,z=10,15,20
print(x,y,z)

x += 5
print(x)
 
x -= 5
print(x)
 
x /= 5
print(x)
 
x %= 5
print(x)

x *= 5
print(x)

x *= z
print(x)
 
x **= 5
print(x)

x //= 3
print(x)
 
#---------------------------------------------------------------------------

values=1,2,3
print(values)

a,b,c=values       #a b c ye değer atadık
print(values)

number=10,20,30,40,50
q,w, *e =number          #e yi sığmayan değerler için iste yaptık
print(q,w,e)
print(q,w,e[1])
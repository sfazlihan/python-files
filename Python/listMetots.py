############################################################################################

letters=['s','t','a','e','p','t','f']
numbers=[2,8,4,6,0,4,9,7]

############################################################################################

               #            numbers listesindeki en küçük değeri yazdırır
max(letters)                #            letters listesinedki en büyük değeri yazdırır
print(min(numbers))
print(numbers)

############################################################################################

numbers[4]=1                #           listenin 4 nolu indisine 1 değerini atadık
print(numbers)

############################################################################################

numbers.append(99)          #           listeye 99 eğerini ekledik
print(numbers)

############################################################################################

numbers.insert(4,50)        #           listenin 4 nolu indisinden önce 50 değeriniekledik
print(numbers)

############################################################################################

letters.pop()               #           listenin son elemanını sildirdik
numbers.pop(5)              #           listenin 5 nolu indisindeki değeri sildirdik
print(letters)
print(numbers)

############################################################################################

letters.remove("t")         #           listeden girilen değeri sildirdik
print(letters)

############################################################################################

numbers.sort()              #           listenin değerlerini küçükten büyüğe doğru sıraladık (numbers)
letters.sort()              #           listenin değerlenini alfabetik sırayla sıraladık (string)
print(letters)
print(numbers)

############################################################################################

letters.reverse()           #           listeyi tersine sıraladık
numbers.reverse()           #           listeyi tersine sıraladık
print(numbers)
print(letters) 

############################################################################################

print(numbers.count(4))     #           Girilen değerin listede kaç tane olduğunu ekrana yazdırır 
print(letters.count('a'))

############################################################################################

numbers.clear()             #           listenin tüm elemanlarını siler
print(numbers)

############################################################################################
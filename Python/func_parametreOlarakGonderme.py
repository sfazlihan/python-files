def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi=="toplama":
        print(f1(2,3))

    elif islem_adi=="cıkarma":
        print(f2(11,2))
        
    elif islem_adi=="carpma":
        print(f3(9,4))
        
    elif islem_adi=="bolme":
        print(f4(28,2))
    else:
        print("geçersiz işlem")
islem(toplama,cıkarma,carma,bolme,"toplama")
islem(toplama,cıkarma,carma,bolme,"cıkarma")
islem(toplama,cıkarma,carma,bolme,"carpma")
islem(toplama,cıkarma,carma,bolme,"bolme")
islem(toplama,cıkarma,carma,bolme,"topXla")
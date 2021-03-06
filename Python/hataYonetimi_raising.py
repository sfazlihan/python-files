# Şifre oluşturma-hata yakalama
import re 
def check_psw(psw):
    if len(psw) > 12:
        raise Exception('Parola 12 karakteri geçmemelidir.')
    elif len(psw) < 8:
        raise Exception('Parola en az 8 karakter olmalıdır.')
    elif not re.search('[a-z]',psw):
        raise Exception('Parola en az 1 küçük harf içermelidir')
    elif not re.search('[A-Z]',psw):
        raise Exception('Parola en az 1 büyük harf içermelidir')
    elif not re.search('[0-9]',psw):
        raise Exception('Parola en az 1 rakam harf içermelidir')
    elif not re.search('[_$%]',psw):
        raise Exception('Parola en az 1 alpha numeric harf içermelidir')
    elif re.search('\s',psw):
        raise Exception('Parola boşluk içermemelidir')
    else:
        print('---Parola geçerli---')
sifre=input('Şifre : ')
check_psw(sifre)



# while True:
#     try:
#         sifre=input('Şifrenizi giriniz...: ')
#         check_psw(sifre)
#     except Exception as ex:
#         print(ex)
#     else:
#         break
#     finally:
#         print('Progress is complated.')
# class Person:
#     def __init__(self,name):
#         self.psw=name
#         if len(self.psw) > 12:
#             raise Exception('Parola 12 karakteri geçmemelidir.')
#         elif len(self.psw) < 8:
#             raise Exception('Parola en az 8 karakter olmalıdır.')
#         elif not re.search('[a-z]',self.psw):
#             raise Exception('Parola en az 1 küçük harf içermelidir')
#         elif not re.search('[A-Z]',self.psw):
#             raise Exception('Parola en az 1 büyük harf içermelidir')
#         elif not re.search('[0-9]',self.psw):
#             raise Exception('Parola en az 1 rakam harf içermelidir')
#         elif not re.search('[_$%]',self.psw):
#             raise Exception('Parola en az 1 alpha numeric harf içermelidir')
#         elif re.search('\s',self.psw):
#             raise Exception('Parola boşluk içermemelidir')
#         else:
#             print('---Parola geçerli---')
# test=Person("Fazlihan%25")
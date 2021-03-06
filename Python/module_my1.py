'''
    Modül 1 
'''

print('Module1 was enjected')

def func1(param):
    return f'back to func object {param}'


class Class1:
    def classFunc(self,name):
        self.name=name
        print(f'Class1 sınıfının fonksiyonu çalışıyor : {self.name}')
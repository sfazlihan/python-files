liste=[1,2,3,4,5]
iterator=iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  #liste elemanlarından fazla komut verirsek hata verir.

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<=self.stop:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration


list=MyNumbers(20,50)
myiter=iter(list)
for i in list:
    print(i)
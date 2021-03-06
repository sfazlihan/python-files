myList = [1,2,3]
myString = "my String"

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie object is created')

    def __str__(self):
        return f'{self.title} by {self.director}'

    def __len__(self):
        return self.duration

    def __del__(self):
        print(f'{self.title} silindi')

m = Movie("Film Adı","Film Yönetmeni",555)

print(str(myList))
print(str(m))

print(len(m))  # Movie classına len metodu eklemeseydik hata verirdi.

del m   # silmeden önce classtaki metodu çalıştırdı.
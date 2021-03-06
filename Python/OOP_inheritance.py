# Inheritance (Kalıtım): Miras Alma

# Person => name, lastname, age, eat(), drink(), run()
# Student(Person), Teacher(Person)

#Animal() => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person created')

    def who_i_am(self):
        print('I am a person')

    def eat(self):
        print('I am eating')
    
 
class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student created')

    # override
    def who_i_am(self):
        print('I am a student')
    
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch=branch

    def who_i_am(self):
        print(f'Hello i am a {self.branch} teacher')
        

p1 = Person('Fazlıhan','Selvitopi')
s1 = Student('Sadık','Turan',7152)
t1 = Teacher('Bizim','Hoca','Science')

print('')

print(f'{p1.firstName} {p1.lastName}')
print(f'{s1.firstName} {s1.lastName} {s1.studentNumber}')

print('')

p1.who_i_am()
s1.who_i_am()
t1.who_i_am()
p1.eat()
s1.eat()
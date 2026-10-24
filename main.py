#6-masala
class Teacher:
    def __init__(self, fullname, subject):
        self.fullname = fullname
        self.subject = subject

    def __repr__(self):
        return f"{self.fullname} - {self.subject} fani o'qituvchisi"

t1 = Teacher("Dilnoza Rahimova", "Informatika")
print(t1)

#7-masala
class Movie:
    def __init__(self, year, title):
        self.year = year
        self.title = title

    def __repr__(self):
        return f"{self.year} - yilda chiqarilgan {self.title} filmi"

m1 = Movie(1991, "Abdullajon")
print(m1)

#8-masala
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __repr__(self):
        return f"{self.name}ning chiqaradigan ovozi: {self.sound} !"

a1 = Animal("Mushuk", "Miyov")
print(a1)

#9-masala
class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __repr__(self):
        return f"{self.name} shahri {self.country} davlatida joylashgan."


city = City("Urganch", "O'zbekiston")
print(city)


# 10-masala
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def __repr__(self):
        return f"{self.brand} noutbuki, tezkor xotirasi: {self.ram} GB"


laptop = Laptop("Lenovo", 16)
print(laptop)

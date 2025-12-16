def greet():
    print("Hello from a function")


def my_function():
    print("Hello from a function")
my_function()


def my_function():
    print("Hello from a function")
my_function()
my_function()
my_function()

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)
temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)
temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
    return "Hello from a function"
message = get_greeting()
print(message)

def get_greeting():
    return "Hello from a function"
print(get_greeting())

def greet():
    print('Hello World!')
#call the function
greet()
print('Outside function')

n = 10
#use pass inside if statement
if n > 10:
    pass
print('Hello')


def future_function():
    pass
#this will execute without any action or error
future_function() 



#function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)
#function call with two values
add_numbers(5, 4)


def greet(name):
    print("Hello", name)
#pass argument
greet("John")

def my_function(name): #name is a parameter
    print("Hello", name)
my_function("Emil") #"Emil" is an argument


def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")



def my_function(name = "friend"):
    print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function(my_person)


#declare global variable
message = 'Hello'
def greet():
    #declare local variable
    print('Local', message)
greet()
print('Global', message)



#outside function
def outer():
    message = 'local'
    #nested function
    def inner():
        #declare nonlocal variable
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)
    inner()
    print("outer:", message)
outer()



def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()


def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)


def factorial(n):
    #Base case
    if n == 0 or n == 1:
        return 1
    #Recursive case
    else:
        return n * factorial(n - 1)
    
print(factorial(5))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(7))


name = input("Enter your name: ")
print("Hello, " + name)







class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()


class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b
    
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name):
        self.name = name
    def printname(self):
        print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.brand)
print(car1.model)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now{self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Emil", 36)
print(p1)




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
    
p1 = Person("Tobias", 36)
print(p1)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")
    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs() 



class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()


class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()


class Outer:
    def __init__(self):
        self.name = "Outer Class"
class Inner:
    def __init__(self):
        self.name = "Inner Class"
    def display(self):
        print("This is the inner class")

outer = Outer()
print(outer.name)


class Outer:
    def __init__(self):
        self.name = "Outer"
class Inner:
    def __init__(self):
        self.name = "Inner"

    def display(self):
        print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()

class Outer:
    def __init__(self):
        self.name = "Emil"
class Inner:
    def __init__(self, outer):
        self.outer = outer

    def display(self):
        print(f"Outer class name:{self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

class Engine:
    def __init__(self):
        self.status = "Off"

    def start(self):
        self.status = "Running"
        print("Engine started")

    def stop(self):
        self.status = "Off"
        print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive() 


class Computer :
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data...")

    class RAM:
        def store(self):
            print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
    x.move() 



class Vehicle :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()



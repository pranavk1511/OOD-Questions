from abc import ABC, abstractmethod

# Classes and object 

class TestClass(): 

    def __init__(self):
        self.name = "Constructor"
        self.desc = "This value is assigned to desc"

    def call_constructor(self):
        print(self.name)
        print(self.desc)

    def assign_values(self,name,desc):
        self.name = name
        self.desc = desc

# Encapuslation 

class TestEncapuslation():
    def __init__(self):
        self.name = "This is to test encapuslation "
        self.desc = "prefixing and atribute with  __ makes it private"

    def __private_method(self):
        print("Private method is being accessed")

    def publicmethod(self):
        print("This is a public method and it should work")
        print("Trying to access private method")
        # accesiing methods inside the class is possible 
        self.__private_method()
    
# Inheritance 

class Animal():

    def __init__(self,name,desc):
        self.name = name
        self.desc = desc

    def print_name(self):
        print(self.name)
        print(self.desc)

class Dog(Animal):

    def __init__(self,age):
        self.age = age
        self.name = "Dog"
        self.desc = "This is a dog"
    
    def print_age(self):
        super().print_name()
        print("Age of Dog : ",self.age)
    
class Cat(Animal):

    def __init__(self,voice):
        self.voice = voice
        self.name = "Cat"
        self.desc = "This is a cat"
    
    def print_voice(self):
        super().print_name()
        print("Voice of Cat : ",self.voice)

# Polymorphism

class Base():

    def print(self):
        print("Base class")

class Derived(Base):

    def print(self):
        print("Derived class")
    
class Derived2(Derived,Base):
    
        def print2(self):
            print("Derived2 class")
    
# Abstract Class

class Vehicle(ABC):
    
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc

    @abstractmethod
    def printDetails(self):
        pass

class Sedan(Vehicle):

    def printDetails(self):
        print(self.name)
        print(self.desc)

    
    
    
# Test Classes and Objects 

# obj = TestClass()
# obj.call_constructor()
# new_name = "Pranav"
# new_desc = "Pranav is studying OOD"
# obj.assign_values(new_name,new_desc) # assigning new value
# obj.call_constructor() # value is updated nnow 

# Test Encapuslation

# when you declare a function with __ it's name gets mangled and thus it throws method not found 
# you can use _TestEncapsulation__private_method() to access the private method
# obj.__private_method()

# obj = TestEncapuslation()
# obj.publicmethod()

# To Test Inheritance

# Use super().function name to call the function and objects from parent class 
# dog = Dog("24")  
# cat = Cat("Meow")

# dog.print_age()
# cat.print_voice()

# To Test Polymorphism

# derived = Derived()
# derived.print()

# derived2 = Derived2()   
# derived2.print()

# dog = Dog("dog","ThIS is a dog")
# dog.make_sound()

# cat = Cat("Billi","This is a cat")
# cat.make_sound()


# To Test Abstract Class

# sedan = Sedan("BMW", "This is BMW")
# sedan.printDetails()





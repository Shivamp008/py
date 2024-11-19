# #SINGLE INHERITANVE --------------> 1
# class Animal:
#     def __init__(self, name, species):
#         self.name = name 
#         self.species = species 

#     def make_sound(self):
#         print("Sound made by the Animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed

#     def make_sound(self):
#         print("Bark!")

# d = Dog("Dog", "Doggerman")
# d.make_sound()

# a = Animal("Dog", "Pitbull")
# a.make_sound()

# #MULTIPLE INHERITANCE ----------------> 2
# class Student:
#     def __init__(self, name):
#         self.name = name 
#     def show(self):
#         print(f"The name of Student is {self.name}.")
# class Dancer:
#     def __init__(self, dancer):
#         self.dancer = dancer
#     def show(self):
#         print(f"You are interested in {self.dancer}")
# class StudentDancer:
#     def __init__(self, name, dancer):
#         self.name = name
#         self.dancer = dancer
#     def show(self):
#         print(f"Your name is {self.name} and your professions is {self.dancer}.")

# a = StudentDancer("Shivam", "Nachna")
# print(a.show())
# print(StudentDancer.mro()) #METHOD

# #Multilevel Inheritance ---------------> 3
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species ="Dog")
#         self.breed = breed 
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")

# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retirement")
#         self.color = color
#     def show_detaisl(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o = GoldenRetriever("Oscar", "Brown")
# o.show_details()

# a = Dog("Oscar", "Pitbull")
# a.show_details()

# #HYBRID INHERITANCE ---------------->
# # Base class
# class Animal:
#     def speak(self):
#         return "Bark"

# # Single Inheritance: Dog inherits from Animal
# class Dog(Animal):
#     def bark(self):
#         return "Danger Zone!"

# # Another Base class
# class Mammal:
#     def feed_milk(self):
#         return "Feeding milk"

# # Multiple Inheritance: Cat inherits from Animal and Mammal
# class Cat(Animal, Mammal):
#     def meow(self):
#         return "CAT: Meow!"

# # Hybrid Inheritance: Pet inherits from Dog and Cat (which already inherit from other classes)
# class Pet(Dog, Cat):
#     def __init__(self, name):
#         self.name = name

# # Testing the classes
# my_pet = Pet("Oscar")
# print(my_pet.speak())     # From Animal class
# print(my_pet.bark())      # From Dog class
# print(my_pet.feed_milk()) # From Mammal class
# print(my_pet.meow())      # From Cat class
# print("Pet name:", my_pet.name)


#HIERACHICAL INHERITANCE ----------->

# Base class
class Vehicle:
    def start_engine(self):
        return "Engine started"

# Derived class 1
class Car(Vehicle):
    def drive(self):
        return "Car is driving"

# Derived class 2
class Motorcycle(Vehicle):
    def ride(self):
        return "Motorcycle is riding"

# Derived class 3
class Truck(Vehicle):
    def haul(self):
        return "Truck is hauling cargo"

# Testing the classes
my_car = Car()
print(my_car.start_engine())   # From Vehicle class
print(my_car.drive())          # From Car class

my_motorcycle = Motorcycle()
print(my_motorcycle.start_engine())   # From Vehicle class
print(my_motorcycle.ride())           # From Motorcycle class

my_truck = Truck()
print(my_truck.start_engine())   # From Vehicle class
print(my_truck.haul())           # From Truck class

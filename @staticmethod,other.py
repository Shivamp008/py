# def add(a, b):
#     return a + b
# # class Math:
# #     @staticmethod
# #     def add(a, b):
# #         return a + b

# x = int(input("Enter a number for add: "))
# y = int(input("Enter another number for add: "))
# # print(Math.add(1, 3))
# print(add(x, y))

#CLASS VARIABLE AND INSTANCE VARIABLE ---------------->
# class Student():
#     marks = 20 #CLASS VARIABLE 
#     noofstudents = 0
#     def __init__(self, name):
#         self.name = name 
#         Student.noofstudents += 1
#     def showdetails(self):
#         print(f"The name of the student is {self.name} and its assignment marks are {self.marks}")
#         print(f"{self.name} are {self.noofstudents} student")

# a = Student("Shivam")
# a.showdetails()
# b = Student("Aditya")
# b.marks = 15 # INSTANCE VALRIABLE
# b.name = "Sushant"
# b.showdetails()

# # CLASS METHODS ------------------------------->
# class Student():
#     std = 9
#     def show(self):
#         print(f"The name of the Student is {self.name} and class is {self.std}")
#     # @classmethod
#     def changestd(cls, newstd):
#         cls.std = newstd

# a = Student()
# a.name = "Shivam"
# # a.std = 9
# a.show()
# a.changestd(10)
# a.show()
# print(Student.std)

# #CLASS METHOD V/S ALTERNATIVE CONSTRUCTOR ------------>
# class Person():
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     @classmethod
#     def from_string(cls, string):
#         name, age = string.split(",")
#         return cls(name, int(age))

# Person = Person.from_string("Shivam, 13")
# print(Person.name, Person.age)

#dir(), dict, help() ----------->
# a = [2,3,4]
# print(dir(a))

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Person("shivam", 13)
# print(p.__dict__)
# print(help(Person))
# cube = lambda x: x*x*x
# a = [2,3,4,5,6,7]
# b = list(map(cube, a))
# print(F"The cube of {a} is {b}")

# def filter_function(a):
#     return (a>3)
# newa = list(filter(filter_function, a))
# print(newa)

# from functools import reduce
# numbers = [1,3,5,7,9,11,13,15,17]
# def mysum(x, y):
#     return x+y

# sum = reduce(mysum, numbers)
# print(sum)

# 'IS' AND '==' USE
# a = 5
# b = "5"
# print(a is b)
# print(a == b)

# PARAMETERIZED CONSTRUCTOR EXAMPLE
# class Person:
#     def __init__(self, name, age):
#         print("Hey I am a person.")
#         self.name = name 
#         self.age = age
#     def info(self):
#         print(f"{self.name} you are {self.age} years old.")

# a = Person("Shivam", 13)
# b = Person("Vishal", 24)
# a.info()
# b.info()

# DEFAULT CONSTRUCTOR EXAMPLE
# class Details:
#     def __init__(self):
#         print("Animal Crab belongs to crustaceans group.")
# obj1 = Details()

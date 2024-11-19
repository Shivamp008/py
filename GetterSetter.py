# GETTER 
# class MyClass:
#     def __init__(self, value):
#         self._value = value

#     def show(self):
#         print(f"Value is {self._value}")

#     @property
#     def ten_value(self):
#         return 10* self._value
    
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10
# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()


# #INHERITANCE_CODE
# class Student():
#     def __init__(self, name, rollno):
#         self.name = name 
#         self.rollno = rollno
#     def showdetails(self):
#         print(f"Hey {self.name}, your school roll number is {self.rollno}")

# class Programmer(Student):
#     def mine(self):
#         print("Hey I changed this name by Pogrammer.")

# a = Student("Shivam", 1)
# a.showdetails()
# b = Programmer("Aditya", 3)
# b.showdetails()
# b.mine()
# # PUBLIC ACCESS SPECIFIER
# class Student():
#     def __init__(self):
#         self.name = "Shivam"
# a = Student()
# print(a.name)

# #PRIVATE ACCESS SPECIFIER
# class Student():
#     def __init__(self):
#         self.__name = "Shivam"
# a = Student()
# # print(a.__name) # CANNOT BE ACCESSED DIRECTLY
# print(a._Student__name) # THIS IS THE WAY TO ACCESS

# print(a.__dir__())

# ##PROTECTED ACCESS SPECIFIER
# class Student():
#     def __init__(self):
#         self._name = "Shivam"
    
# a = Student()
# print(a._name)
# print(dir(Student))


#Rectangle Area:
name = input("What is your name? : ")
print(f"Hello {name}! Nice to meet you.")
print("\nThis is about Rectangle Area and Perimeter\n")
print("1 for Rectangle Area")
print("2 for Rectangle Perimeter")

# Remove unnecessary definitions of area and parameter as integers.
choice = input("\nWhat do you want to find - 'area' or 'perimeter': ").strip().lower()

if choice == 'area':
    length = float(input("Enter the length of the Rectangle: "))
    breadth = float(input("Enter the breadth of the Rectangle: "))
    area = length * breadth
    print("The area of the Rectangle is", area)

elif choice == 'perimeter':
    length = float(input("Enter the length of the Rectangle: "))
    breadth = float(input("Enter the breadth of the Rectangle: "))
    perimeter = 2 * (length + breadth)
    print("The perimeter of the Rectangle is", perimeter)

else:
    print("Invalid choice. Please enter 'area' or 'perimeter'.")
    
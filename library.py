# class library:
#     def __init__(books, count, no_of_book):
#         books.count = count
#         books.no_of_book = no_of_book
#     def find(books):
#         print(f"The Number of Book in Library is {books.count} books")

# count = ["Register", "Copy", "NCERT", "Black Book"]
# no_of_book = len(count)
# if no_of_book == len(count):
#     print("There is not any problem in library")
# else:
#     raise RuntimeError("There is not any problem in library")

# a = library(count, no_of_book)
# print(a.count)

# find = check(no_of_book, len(count))
# if no_of_book == find:
#     print("There is not any mistake.")
# else:
#     raise ValueError("Some Books are not not there.")

# print(len(count))

# a = int(input("Enter a number for add: "))
# b = int(input("Enter another number for add: "))
# def add(a, b):
#     return a + b
# print(add(a, b))

def add(a, b):
    return a + b
# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

x = int(input("Enter a number for add: "))
y = int(input("Enter another number for add: "))
# print(Math.add(1, 3))
print(add(x, y))
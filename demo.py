# a = 5 

# def hello():
#     global a
#     a = 10
#     print(f"The local a is {a}")

# print(f"The global a is {a}")
# print("Hello Shivam!")
# print(a)
# hello()

# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# a = int(input("Enter a number: "))
# b = input()
# cube = lambda x: x*x*x 
# if a == b:
#     raise ValueError("please Enter a number not a string.")
# print(cube(a))

# FUNCTION IN FUNCTION 
# def appl(fx, value):    
#     return 6 + fx(value)

# cube = lambda x: x*x*x 
# print(appl(cube, 7))

# OPERATOR OVERLOADING ----------->

class vector:
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b 
        self.c = c 
    def __str__(self):
        return f"{self.a}a + {self.b}b + {self.c}c"
    
    def __add__(self, i):
        return vector(self.a + i.a , self.b + i.b, self.c + i.c)

v1 = vector(2,3,4)
print(v1)
v2 = vector(2,4,5)
print(v2)
print(v1 + v2) 
print(type(v1 + v2))
class Person():
    def __init__(self, name):
        self.name = name 

    def __len__(self):
        i = 0 
        for a in self.name:
            i = i + 1
        return i
    
    def __str__(self):
        return f"The name of the person is {self.name} "

    def __repr__(self):
        return f"Person('{self.name}') "
    
    def __call__(self):
        print("Hii I am there.")

# a = float(input("Enter number: "))
# b = float(input("Enter number: "))
# print(a*b)
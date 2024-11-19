class ParentClass:
    def parent_method(self):
        print("This is the parent class.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Shivam")
    def child_method(self):
        print("This is the child class.")
        super().parent_method()

child_object = ChildClass()
child_object.parent_method()
child_object.child_method()

# magic/dunder method --------->
# class Person():
#     name  = "shivam"
#     # name1 = "Priyanshi"
#     def __len__(self):
#         i = 0 
#         for a in self.name:
#             i = i + 1
#         return i

# p = Person()
# print(p.name)
# # print(p.name1,", This is the index of your given name:", len(p.name1))
# print(len(p))

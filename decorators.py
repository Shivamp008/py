# def greet(fx):
#     def fxm():
#         print("Good morning!")
#         fx()
#         print("Thanks for using this code.")
#     return fxm
# # @greet
# def hello():
#     print("Hii Everyone!")
# greet(hello)()
# #hello()

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good morning!")
#         fx(*args, **kwargs)
#         print("Thanks for using my code!")
#     return mfx 
# @greet
# def add(a, b):
#     print(a + b)
# # greet(add)(1,3)
# add(1,3)


#YET THIS CODE IS NOT WORKING
# import logging 
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} retuned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a+b

def greet(fx):
    def mfx(*args, **kwargs):
        print("Welcome to my calculator")
        fx(*args, **kwargs)
        print("Bye bye")
    return mfx

@greet
def add(a, b):
    print(a+b)
add(3, 5)
X = 10
Y = 20
Z = X+Y

"""
Adds numbers and returns them
"""
def add_numbers(a,b):
    return a+b

"""
Greets the user with a hello message
"""
def greet(name):
    print("Hello, " + name + "!")

"""
Class used to store user name and age
"""
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

"""
Returns division of a and b, with a 0 check
"""
def divide(a, b):
    if b != 0:
        return "Error"
    return a/b

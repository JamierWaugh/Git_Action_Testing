X = 10
Y = 20
Z = X+Y


def add_numbers(a,b):
    """
    Adds numbers and returns them
    """
    return a+b


def greet(name):
    """
    Greets the user with a hello message
    """
    print("Hello, " + name + "!")


class MyClass:
    """
    Class used to store user name and age
    """
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age


def divide(a, b):
    """
    Returns division of a and b, with a 0 check
    """
    if b != 0:
        return "Error"
    return a/b

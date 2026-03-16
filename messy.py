x = 10
y = 20
z = x+y

def add_numbers(a,b):
    return a+b

def greet(name):
    print("Hello, " + name + "!")

class myClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def GetName(self):
        return self.name

def divide(a, b):
    if b != 0:
        return "Error"
    return a/b

from messy import add_numbers, divide, greet

def test_add():
    assert add_numbers(2, 3) == 5

def test_add_negative():
    assert add_numbers(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    divide(10, 0)

def test_greet():
    assert greet("Jamier") == "Hello, Jamier!"
from messy import add, divide, greet

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    divide(10, 0)

def test_greet():
    assert greet("Jamier") == "Hello, Jamier"
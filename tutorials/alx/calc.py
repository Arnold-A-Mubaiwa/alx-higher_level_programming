def add(a, b):
    """Add function"""
    return a + b

def subtract(a, b):
    """Subtract function"""
    return a - b

def multiply(a, b):
    """Multipy function"""
    return a * b

def divide(a, b):
    """Divide function"""
    if b == 0:
        raise ValueError("Can not divide by 0")
    return a / b

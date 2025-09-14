def add(a, b):
    return a + b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None

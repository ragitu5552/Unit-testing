def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero")
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("Invalid Input")
    return a/b

if __name__ == "__main__":
    print(divide(5,5))
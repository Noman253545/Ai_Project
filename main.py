import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Negative input for square root"
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "Error: Non-positive input for logarithm"
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")

    choice = input("Enter choice (1-10): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", exponentiate(num1, num2))

    elif choice == '6':
        num = float(input("Enter number: "))
        print("Result:", square_root(num))

    elif choice == '7':
        num = float(input("Enter number: "))
        base: float = float(input("Enter base (default is 10): ") or 10)
        print("Result:", logarithm(num, base))

    elif choice in ['8', '9', '10']:
        angle = float(input("Enter angle in degrees: "))
        if choice == '8':
            print("Result:", sine(angle))
        elif choice == '9':
            print("Result:", cosine(angle))
        elif choice == '10':
            print("Result:", tangent(angle))
    else:
        print("Invalid Input")

if __name__ == "__main__":
    calculator()

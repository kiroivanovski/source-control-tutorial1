def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if x == 0 or y==0:
        return "Division by zero is not allowed."
    return x / y


print("Simple Calculator")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))


# 1. Vo fajlovite ima greski. Kreirajte nov branch so ime bug_fixing kade ke gi pronajdete greskite i popravete gi.
# Otkako ke gi pronajdete zacuvajte gi promenite vo bug_finxing branchot

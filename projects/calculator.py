# mhmd amin

# first we add our project functions
# 1- function to add two nums
def add(x, y):
    return x + y
# 2- function to subtract two nums
def subtract(x, y):
    return x - y
# 3- function to multiply two nums
def mult(x, y):
    return x * y
# 4- function to divide two nums
def div(x, y):
    return x/y

# the program

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    while True:
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
# take input from the user
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ("1", "2", "3", "4"):
            break
        else:
            print("Invalid choice, try again.")

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", mult(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", div(num1, num2))

    else:
        print("Invalid Input")
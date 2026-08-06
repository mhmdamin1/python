print("hi i am mohamed nice to meet u.")
# Function to print binary number using recursion
def convertTObin(x):
    if x > 1:
        convertTObin(x // 2)
    print(x % 2, end='')


# dec num
dec = int(input("enter your number: "))
convertTObin(dec)
print()

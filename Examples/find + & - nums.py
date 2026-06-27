# take the list from user
numbers = [int(x) for x in input("enter your list nums: ").split()]
# sort the list
numbers.sort()
print("list: ", numbers)
# check numbers
for x in numbers:
    if x > 0:
        print(f"{x} is positive")
    else:
        print(f"{x} is negative")

###################################################################################################################

# basic example
x = int(input("enter your list nums: "))

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is = 0")
else:
    print("x is negative")
# mhmd amin
# take input from user

x = int(input("enter number: "))

if x == 0 or x == 1:
    print(x, "the number is not prime num.")
elif x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            print(x, "is not prime number")
            break
        else:
            print(x, "is a prime number")
            break

# if the number less than 1 and 0
else:
    print(x, "is not prime number")




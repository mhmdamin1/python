# mohamed Amin / محمد امين
# we will do the swaping by 2 ways
# 1
a = int(input("enter first num  "))
b = int(input("enter secound num  "))

print(f"the nums before swaping are:{a} & {b} ")
# just use new variable to store the data in it
temp = a
a = b
b = temp
print(f"the nums after swaping are:{a} & {b} ")


# 2

#a = int(input("enter first num  "))
#b = int(input("enter secound num  "))


print(f"before swaping: a = {a} , b = {b}")
# do not forget the f in the() tells python that the letters in the {} is variables not strings.
a, b = b, a
print(f"before swaping: a = {a} , b = {b}")
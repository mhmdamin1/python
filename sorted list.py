#mohamed amin

n = int(input("How many numbers will you enter? "))

# Step 2: Create empty list and fill it using a for loop
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Step 3: Sort the list using nested for loop (Selection Sort)
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            # Swap values
            numbers[i], numbers[j] = numbers[j], numbers[i]



print("Sorted list:", numbers)
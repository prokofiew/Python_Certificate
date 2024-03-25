swapped = True
numbers = []
amount = int(input("How many numbers would you like to add: "))

for i in range(amount):
    val = int(input("Enter number to add: "))
    numbers.append(val)

print(numbers)

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            swapped = True
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print("Sorted")
print(numbers)



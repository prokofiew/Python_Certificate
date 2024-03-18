# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # in python warunek niezerowy jest uznawany jako True
    # while number:
    # Check if the number is odd.
    # if number % 2: jest także zgodne bo daje logiczną jedynkę lub 0
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
# ===========================================================================

odd_numbers2 = 0
even_numbers2 = 0

number1 = int(input("Enter a number: "))

while number1:
    if number1 % 2:
        print("Odd number")
        odd_numbers2 += 1
    else:
        print("Even number")
        even_numbers2 += 1
    number1 = int(input("Enter a number: "))

print("Odd numbers: ", odd_numbers2)
print("Even numbers", even_numbers2)

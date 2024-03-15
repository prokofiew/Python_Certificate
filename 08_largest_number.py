# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))
# number_3 = int(input("Enter the third number: "))

# if number_1 > number_2:
#     if number_1 > number_3:
#         largest_number = number_1
#     else:
#         largest_number = number_3
# elif number_2 > number_3:
#     if number_2 > number_1:
#         largest_number = number_2
#     else:
#         largest_number = number_1
# elif number_3 > number_1:
#     if number_3 > number_2:
#         largest_number = number_3
#     else:
#         largest_number = number_2
#
# print(largest_number)
#
#
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# largest_number = number1
#
# if number2 > largest_number:
#     largest_number = number2
# if number3 > largest_number:
#     largest_number = number3
#
# print("The largest number is:", largest_number)

# Read three numbers.
number4 = int(input("Enter the first number: "))
number5 = int(input("Enter the second number: "))
number6 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number2 = max(number4, number5, number6)

# Print the result.
print("The largest number is:", largest_number2)

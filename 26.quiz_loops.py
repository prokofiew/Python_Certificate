__question_1__ = """
Create a for loop that counts from 0 to 10, 
and prints odd numbers to the screen. """

# for i in range(0, 11):
#     if i % 2 != 0:
#         print(i)

__question_2__ = """
Create a while loop that counts from 0 to 10, 
and prints odd numbers to the screen. """
#
# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

__question_3__ = """
Create a program with a for loop and a break statement.
The program should iterate over characters in an email address, 
exit the loop when it reaches the @ symbol, 
and print the part before @ on one line.  """

# for char in "john.smith@pythoninstitute.org":
#     if char == "@":
#         break
#     print(char, end="")


__question_4__ = """
Create a program with a for loop and a continue statement. 
The program should iterate over a string of digits, replace each 0 with x, 
and print the modified string to the screen.:
"""
for num in "0165031806510":
    if num == "0":
        print("x", end="")
        continue
    print(num, end="")




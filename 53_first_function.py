__code__ = """
code for decomposition:

print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())
"""


# from course
def message():
    print("Enter a value")


message()
d = int(input())
message()
e = int(input())
message()
f = int(input())


# mine
def ask_for_value():
    a = int(input("Please enter a value: "))
    return a


a = ask_for_value()
b = ask_for_value()
c = ask_for_value()

print(a, b, c)

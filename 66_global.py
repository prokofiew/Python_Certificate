def my_function():
    global var
    var = 2
    print("This is inside function: ", var)


var = 1
print("Before function: ", var)
my_function()
print("Outside function", var)


def my_function2(n):
    print("I got", n)
    n += 1
    print("I have", n)


var1 = 1
my_function2(var1)
print(var1)
__comment__ = """
return without and with an expression
"""


def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


happy_new_year()


def boring_func():
    return 123


x = boring_func()

print("Function returns a value:", x)


# no usage of returned value
def boring_function():
    print("'Boredom Mode' ON.")
    return 123


print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")

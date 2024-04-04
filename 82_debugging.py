value = input('Enter a natural number: ')
if value.isdigit():
    value = int(value)
    if type(value) is int:
        print('The reciprocal of', value, 'is', 1 / value)
else:
    print("Wrong value: ", value)

# second version:
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1 / value)

except ValueError:
    print("Wrong value")
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Strange thing happened ... sorry")


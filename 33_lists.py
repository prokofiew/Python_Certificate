numbers = [10, 5, 7, 2, 1]

print("Original list: ", numbers)

numbers[0] = 111
print("New list: ", numbers)

numbers[1] = numbers[4]
print("Copied 5th to 2nd element: ", numbers)

# accessing list element
print("First element: ", numbers[0])
print("Last element: ", numbers[-1])

# printin list length
print("List length: ", len(numbers))

# removing items
print(numbers)
del numbers[1]
print("=============================")
print("List after deletion")
print(numbers)
print("List length: ", len(numbers))



numbers = [111, 7, 2, 1]
print("Len:", len(numbers))
print(numbers)

##################################

numbers.append(4)
print("Len:", len(numbers))
print(numbers)

##################################

numbers.insert(1, 222)
print("Len:", len(numbers))
print(numbers)

##################################

my_list = []
for i in range(5):
    my_list.append(i + 1)

print(my_list)

##################################

my_list_2 = []
for i in range(5):
    my_list_2.insert(0, i + 1)
print("Len:", len(my_list_2))
print(my_list_2)
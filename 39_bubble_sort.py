my_list = [8, 10, 6, 2, 4]
# for i in range(len(my_list) - 1):
#     if my_list[i] > my_list[i + 1]:
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list)


swapped = True
counter = 0
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        print(my_list)
        counter += 1
print(my_list)
print(counter)

# ===========================================================

my_list3 = [6, 2, 1, 10, 8]
print(my_list3)
my_list3.sort()
print(my_list3)

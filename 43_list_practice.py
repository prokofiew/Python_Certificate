my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
    # print(i)

print(largest)


largest2 = 0
for i in my_list:
    if i > largest2:
        largest2 = i

print(largest2)

# ==============================================

my_list2 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest3 = my_list2[0]
# slice used to avoid comparing first element with itself
for i in my_list2[1:]:
    if i > largest3:
        largest3 = i

print(largest3)
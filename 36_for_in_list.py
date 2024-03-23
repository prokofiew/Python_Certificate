my_list = [10, 1, 8, 3, 5]
total_1 = 0
total_2 = 0

for i in range(len(my_list)):
    total_1 += my_list[i]
print(total_1)


# !!!!!!!!!! BETTER !!!!!!!!!!!!!
for i in my_list:
    total_2 += i
print(total_2)

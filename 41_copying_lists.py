my_list1 = [1]
my_list2 = my_list1
my_list1[0] = 2
print(my_list2)

# slice
my_list3 = [1]
my_list4 = my_list3[:]
my_list3[0] = 3
print(my_list4)

my_list5 = [10, 8, 6, 4, 2]
my_list6 = my_list5[0:5]  # 5 is not included
my_list7 = my_list5[1:4]  # 4 is not included
my_list8 = my_list5[1:-1]
my_list9 = my_list5[-1:1]  # will make empty slice
my_list10 = my_list5[:3]  # from index 0 to 3

print(my_list6)
print(my_list7)
print(my_list8)

new_list = [10, 8, 6, 4, 2]
del new_list[1:3]  # del elements on 1st and 2nd index
print(new_list)
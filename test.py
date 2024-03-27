my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
    # print(v, my_list)
print(my_list)

my_list2 = [i for i in range(-1, 2)]

print(my_list2)

t = [[3-i for i in range(3)] for j in range (3)]
s = 0
print(t)
for i in range(3): # przejście po przekątnej macierzy
    s += t[i][i]
    # print(t[i][i])
print(s)

# my_list3 = [[0, 1, 2, 3] for i in range(2)]
# print(my_list3[2][0])

def sum_list(lst):
    total = 0

    for elem in lst:
        total += elem

    return total


print(sum_list([2, 3, 4]))


def strange_function(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_function(5))

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

# BUT BETTER

variable_x = 1
variable_y = 2

variable_x, variable_y = variable_y, variable_x

# ==========================================================

my_list = [10, 1, 8, 3, 5]
print(my_list)

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# ===========================================================

__comment__ = """
we've launched the for loop to run through its body length // 2 times 
(this works well for lists with both even and odd lengths, 
because when the list contains an odd number of elements, 
the middle one remains untouched)
"""
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print(my_list)

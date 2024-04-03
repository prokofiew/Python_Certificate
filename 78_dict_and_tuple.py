my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

empty_tuple = ()
print(type(empty_tuple)) # outputs: <class 'tuple'>

one_elem_tuple_1 = ("one", ) # Brackets and a comma.
one_elem_tuple_2 = "one", # No brackets, just a comma.

my_tuple_1 = 1,
print(type(my_tuple_1))  # outputs: <class 'tuple'>

my_tuple_2 = 1  # This is not a tuple.
print(type(my_tuple_2))  # outputs: <class 'int'>

my_tuple_3 = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple_3[2] = "guitar" # The TypeError exception will be raised.


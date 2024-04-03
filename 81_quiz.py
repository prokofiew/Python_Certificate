tup = 1, 2, 3
a, b, c = tup

print(a * b * c)







__answer__ = """
The program will print 6 to the screen.
The tup tuple elements have been "unpacked" 
in the a, b, and c variables.
"""



__question1__ = """
3: Complete the code to correctly use
the count() method to find the number
of duplicates of 2 in the following tuple.
"""

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates =  # Write your code here.
#
# print(duplicates)  # outputs: 4


__answer1__ = """
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)    # outputs: 4
"""

__question2__ = """
Write a program that will "glue"
the two dictionaries(d1 and d2)
together and create a new one(d3).
"""

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

__question3__ = """
Write a program that will
convert the colors tuple
to a dictionary.
"""

colors = (("green", "#008000"), ("blue", "#0000FF"))

# solution 1
colors_dict = {}
for elem in colors:
    colors_dict.update({elem[0]: elem[1]})

# solution 2
colors_dictionary = dict(colors)

print(colors_dict)
print(colors_dictionary)
__scenario__ = """
The Beatles were one of the most popular music groups of the 1960s, 
and the best-selling band in history. 
Some people consider them to be the most influential act of the rock era. Indeed, 
they were included in Time magazine's compilation of the 20th Century's 100 most influential people.

The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, 
Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).

Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

    step 1: create an empty list named beatles;
    step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, 
            and George Harrison;
    step 3: use the for loop and the append() method to prompt the user to add the following members of the band 
            to the list: Stu Sutcliffe, and Pete Best;
    step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
    step 5: use the insert() method to add Ringo Starr to the beginning of the list.

"""

beatles = []
new_members = []

while True:
    user_input = input("Enter name of band member: ")
    if user_input == "0":
        print(beatles)
        break
    else:
        beatles.append(user_input)

while True:
    user_input = input("Enter name of band member: ")
    if user_input == "0":
        print(beatles)
        break
    else:
        new_members.append(user_input)

for member in new_members:
    beatles.append(member)
print(beatles)

# del beatles[3:5]
del beatles[-2:]
print("after deletion: ", beatles)


beatles.insert(0, input("Enter a beatles to enter to the begining of the list: "))
for i in beatles:
    print(i, end=",")




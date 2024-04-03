pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
}

item_1 = pol_eng_dictionary["gleba"]  # ex. 1
print(item_1)  # outputs: soil

item_2 = pol_eng_dictionary.get("woda")  # ex. 2
print(item_2)  # outputs: water


# removing items
print(len(pol_eng_dictionary))  # outputs: 3
del pol_eng_dictionary["zamek"]  # remove an item
print(len(pol_eng_dictionary))  # outputs: 2

pol_eng_dictionary.clear()  # removes all the items
print(len(pol_eng_dictionary))  # outputs: 0

del pol_eng_dictionary  # removes the dictionary


# copying
copy_dictionary = pol_eng_dictionary.copy()
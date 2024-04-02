dictionary = {"dog": "chien", "cat": "chat", "horse": "cheval"}

dictionary["cat"] = "minou"
print(dictionary)

# sorting
for key in sorted(dictionary.keys()):
    print(key)

for value in dictionary.values():
    print(value)

dictionary["swan"] = "cygne"
dictionary.update({"frog": "lafroge"})
print("added to dictionary:\n", dictionary, sep="")
print("\nremoved dog and last item:")
del dictionary["dog"]
# remove last item
dictionary.popitem()
print(dictionary)


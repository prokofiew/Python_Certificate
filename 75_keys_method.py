dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

print("\nitems()")
for key, value in dictionary.items():
    print(key, "->", value)


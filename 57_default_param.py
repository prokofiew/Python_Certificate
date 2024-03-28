def introduction(name, surname="Smith"):
    print("Hello, my name is:", name, surname)


introduction("John")
introduction("Alan", "Harper")


def introduction_2(name="John", surname="Smith"):
    print("Hello, my name is:", name, surname)


introduction_2()
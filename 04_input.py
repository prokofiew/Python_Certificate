print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")


anything2 = input("Tell me anything...")
print("Hmm...", anything2, "...Really?")

# input result is string, this will not work
# anything3 = input("Enter a number: ")
# something = anything3 ** 2.0
# print(anything3, "to the power of 2 is", something)

anything4 = float(input("Enter a number: "))
something1 = anything4 ** 2.0
print(anything4, "to the power of 2 is", something1)


leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
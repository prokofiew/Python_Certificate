# f_nam = input("May I have your first name, please? ")
# l_nam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + f_nam + " " + l_nam + ".")


print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

flag_register = 0x1234
the_mask = 8  # Bit mask to check the state of the third bit
binary_representation = bin(flag_register)
mask_bit = bin(the_mask)
print("Flag ", binary_representation)
print("Mask: ", mask_bit)

result = flag_register & the_mask


if flag_register & the_mask:
    print("My bit is set.")
    print("Result ", bin(result))
    print("Result ", result)

else:
    print("My bit is reset.")
    print("Result ", bin(result))
    print("Result ", result)


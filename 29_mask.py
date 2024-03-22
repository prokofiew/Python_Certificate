flag_register = 0x1234
the_mask = 8

flag_register = flag_register & ~the_mask
print(flag_register)

flag_register &= ~the_mask

print(flag_register)

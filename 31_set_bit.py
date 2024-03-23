flag_register = 0b00000000000000000000000000000000
mask = 0b00000000000000000000000000000100

# flag_register |= mask
flag_register2 = flag_register ^ mask
print("Flag : ", bin(flag_register))
print("Flag | mask: ", bin(flag_register2))  # Wyświetlenie wartości flag_register w postaci binarnej



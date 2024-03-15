# Basic operators
#
# An operator is a symbol of the programming language, which is able to operate on the values.
#
# EXPRESSION: Remember: Data and operators when connected together form expressions. The simplest expression is a literal itself.
#
# ORDER:
#
# +
# -
# *
# /
# //
# %
# **
#
# ==============================================================================
# Remember: It's possible to formulate the following rules based on this result:
#
#     - when both ** arguments are integers, the result is an integer, too;
#     - when at least one ** argument is a float, the result is a float, too.
#
# !!!!!!!!!!!!!
# The result produced by the division operator is always a float, regardless of whether or not the result seems to be a float at first glance: 1 / 2, or if it looks like a pure integer: 2 / 1.
#
#
# Integer division (floor division)
#
# A // (double slash) sign is an integer division operator. It differs from the standard / operator in two details:
#
#     - its result lacks the fractional part ‒ it's absent (for integers), or is always equal to zero (for floats); this means that the results are always rounded;
#     - it conforms to the integer vs. float rule.


print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

# OUTPUT:
# 2
# 2.0
# 2.0
# 2.0

# !!!!!!!!!!
# This is very important: rounding always goes to the lesser integer.
print(6 // 4)
print(6. // 4)

# OUTPUT:
# 1
# 1.0
#
# =================
print(-6 // 4)
print(6. // -4)

# OUTPUT:
# -2
# -2.0
#
# The result is two negative twos. The real (not rounded) result is -1.5 in both cases. However, the results are the subjects of rounding. The rounding goes toward the lesser integer value, and the lesser integer value is -2, hence: -2 and -2.0.
#
# Integer division can also be called floor division. You will definitely come across this term in the future.
#
#
# HIERARCHY OF PRIORITIES: The phenomenon that causes some operators to act before others is known as the hierarchy of priorities.
#
# Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from left to right.
#
# The result clearly shows that the exponentiation (**) operator uses right-sided binding.
print(2 ** 2 ** 3)
# 2 ** 3 → 8; 2 ** 8 → 256


print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

# output:
# -9 bo ** ma wyższy priorytek i python wykonuje to tak jak to -(3 ** 2)
# -8
# -9

#
# 1   **
# 2   +, - (note: unary operators located next to the right of the power operator bind more strongly)     unary
# 3   *, /, //, %
# 4   +, -    binary

# *** A unary operator is an operator with only one operand, e.g., -1, or +3.
#
# *** A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.


print(2 * 3 % 5)
# # output: 1
#
# EXAMPLES:
print((2 ** 4), (2 * 4.), (2 * 4))
#
# OUTPUT:
# 16 8.0 8
#
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
#
# OUTPUT:
# -0.5 0.5 0 -1
#
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
#
# OUTPUT:
# -2 2 512
__comment__ = """
as two is the base for binary numbers (not 10), 
shifting a value one bit to the left thus corresponds to multiplying it by two; respectively, 
shifting one bit to the right is like dividing by two (notice that the rightmost bit is lost).

The shift operators in Python are a pair of digraphs: << and >>, 
clearly suggesting in which direction the shift will act.

value << bits
value >> bits
 
The left argument of these operators is an integer value whose bits are shifted. 
The right argument determines the size of the shift.

It shows that this operation is certainly not commutative.

The priority of these operators is very high.

Note:

    17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 
    (shifting to the right by one bit is the same as integer division by two)
    17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 
    (shifting to the left by two bits is the same as integer multiplication by four)

"""

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
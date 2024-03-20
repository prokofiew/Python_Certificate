# Example 1:
var = 1
print(var > 0)
print(not (var <= 0))

# Example 2:
print(var != 0)
print(not (var == 0))

__comment__ = """
You may be familiar with De Morgan's laws. 
They say that:

The negation of a conjunction 
is the disjunction of the negations.

The negation of a disjunction is 
the conjunction of the negations.

Let's write the same thing using Python:

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

Note how the parentheses have been used to code the expressions ‒ 
we put them there to improve readability.

We should add that none of these two - 
argument operators can be used in the abbreviated form known as op =.
This exception is worth remembering.
"""

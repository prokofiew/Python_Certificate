squares = [x ** 2 for x in range(10)]

twos = [2 ** i for i in range(10)]

odds = [x for x in squares if x % 2 != 0]

print(squares)

print(twos)

print(odds)

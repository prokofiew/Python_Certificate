def is_triangle(a, b, c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True


# compact version
def is_triangle2(a, b, c):
    return a + b > c and b + c > a and a + c > b


# using or
def is_triangle3(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


def pythagorean_theorem(a, b, c):
    if not is_triangle3(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2

    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_triangle3(a, b, c):
        return None
    return heron(a, b, c)


# a = int(input("Enter a first side of the triangle: "))
# b = int(input("Enter a 2nd side of the triangle: "))
# c = int(input("Enter a 3rd side of the triangle: "))


# if is_triangle(a,b,c):
#     print("Yes, it's a triangle")
# else:
#     print("It's not a triangle")


print(pythagorean_theorem(5, 3, 4))
print(pythagorean_theorem(1, 3, 4))
print(area_of_triangle(1., 1., 2. ** .5))

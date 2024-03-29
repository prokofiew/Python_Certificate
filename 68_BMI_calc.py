def bmi_calc(weight, height):
    return weight / height ** 2


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None
    return weight / height ** 2


def lb_to_kg(lb):
    lb_kg_value = 0.45359237
    return lb * lb_kg_value


def feet_and_inch_to_meter(ft, inch = 0.0):
    foot = 0.3048
    inch_value = 0.0254
    return ft * foot + inch * inch_value


print("First func: ", bmi_calc(99, 1.78))
print("Second func: ", bmi(99, 2.6))
print("American metrics", bmi(weight=lb_to_kg(176), height=feet_and_inch_to_meter(5,7)))





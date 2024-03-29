def leap_year_func(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_data = [1900, 2000, 2016, 1987]
test_result = [False, True, True, False]
result_data = []

for i in range(len(test_data)):
    yr = test_data[i]
    x = leap_year_func(yr)
    result_data.append(x)
    if x == test_result[i]:
        print(yr, "---->", x, "Test OK")
    else:
        print(yr, "---->", x, "Test Failed")


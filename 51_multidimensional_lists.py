import random

__comment__ = """
Imagine that you're developing a piece of software for an automatic weather station. 
The device records the air temperature on an hourly basis and does it throughout the month. 
This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.

First, you have to decide which data type would be adequate for this application. 
In this case, a float would be best, since this thermometer is able 
to measure the temperature with an accuracy of 0.1 ℃.

Then you take an arbitrary decision that the rows will record the readings every hour on the hour 
(so the row will have 24 elements) and each of the rows will be assigned to one day of the month 
(let's assume that each month has 31 days, so you need 31 rows). 
"""
# temperature = [[round(random.uniform(-20, 30), 1) for hour in range(24)] for day in range(31)]
temperature = [[0.0 for hour in range(24)] for day in range(31)]

for day in range(31):
    for hour in range(24):
        temperature[day][hour] = round(random.uniform(-20,30), 1)

# displaying matrix
for i in temperature:
    print(i)

# counting average
total = 0.0
for day in temperature:
    total += day[11]
average = total / 31
print("Average: ", round(average, 1))


# highest temperature in month
highest = -100
for day in temperature:
    for temp in day:
        if temp > highest:
            highest = temp

print("Highest: ", highest)

# count days with temperature equal or higher than 20
counter = 0
for day in temperature:
    for temp in day:
        if temp >= 20.0:
            counter += 1
print("Days with +/= 20 C: ", counter)

# count days with temperature +/= 20 C at noon
counter2 = 0
for day in temperature:
    if day[11] > 20.0:
        counter2 += 1
print("Days with +/= 20 temp at noon: ", counter2)

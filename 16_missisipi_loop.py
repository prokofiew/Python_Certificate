import time


def timer():
    time.sleep(1)


for i in range(1, 6):
    timer()
    print(i, "Mississippi")
print("Ready or not, here I come!")
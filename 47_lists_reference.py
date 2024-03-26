__comment__ = """"
del list_2 usuwa referencję list_2, ale nie usuwa samej listy ani referencji list_3, więc list_3 nadal wskazuje na ten sam obiekt listy.
print(list_3) wydrukuje listę, którą list_3 wskazuje, czyli ["B", "C"].
"""

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)


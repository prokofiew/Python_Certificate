__comment__ = """
W obu przypadkach mamy funkcję my_function, która jako argument przyjmuje listę my_list_1. 
W obu przypadkach przekazujemy do tej funkcji listę my_list_2, ale istnieją subtelne różnice, 
które wpływają na to, jak te dwie funkcje zachowują się:
"""

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]  # Tworzenie nowej listy i przypisanie jej do zmiennej my_list_1
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

__comment2__ = """

W tym przypadku:

    Funkcja my_function otrzymuje listę my_list_2 jako argument my_list_1.
    W linii my_list_1 = [0, 1] zmieniamy referencję zmiennej my_list_1, aby wskazywała na nową listę [0, 1]. Ta operacja nie wpływa na my_list_2, ponieważ jest to tylko nowe przypisanie zmiennej lokalnej w funkcji.
    W efekcie wypisujemy dwie różne listy: my_list_1 z linii 1 i my_list_2.
    Po zakończeniu funkcji my_list_2 nadal wskazuje na pierwotną listę [2, 3], ponieważ nie została ona zmieniona w funkcji.
"""


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_3)
    del my_list_1[0]  # Usunięcie pierwszego elementu z listy przekazanej do funkcji
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_3)


my_list_3 = [2, 3]
my_function(my_list_3)
print("Print #5:", my_list_3)

__comment3__ = """

W tym przypadku:

    Ponownie funkcja my_function otrzymuje listę my_list_2 jako argument my_list_1.
    Linia del my_list_1[0] zmienia bezpośrednio listę, na którą wskazuje my_list_1, 
    usuwając jej pierwszy element. Ponieważ my_list_1 i my_list_2 wskazują na tę samą listę w pamięci, 
    ta operacja zmienia listę zarówno dla my_list_1, jak i my_list_2.
    Dlatego po zakończeniu funkcji zmiany dokonane w my_list_1 są widoczne także w my_list_2, 
    co jest widoczne w linii print("Print #5:", my_list_2).
"""

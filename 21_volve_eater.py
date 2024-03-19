user_word = input("Enter a word: ").upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    print(letter)


# ===============================================================================================================
# 1. `user_word = input("Enter a word: ").upper()`:
# Program prosi użytkownika o wprowadzenie słowa, które jest przechowywane w zmiennej `user_word`. `.upper()`
# jest używane do przekształcenia wszystkich liter w słowie na wielkie litery,
# aby uniknąć problemu z rozróżnianiem małych i wielkich liter w dalszej części kodu.
#
# 2. Pętla `for letter in user_word:`:
# Przechodzi przez każdą literę w słowie wprowadzonym przez użytkownika.
# Na początku, `letter` będzie równa "G".
#
# 3. Warunek `if letter == "A":`, `elif letter == "E":`, itd.:
# Sprawdza, czy aktualna litera to samogłoska (A, E, I, O, U).
# Jeśli tak, to `continue` pomija resztę pętli dla obecnej litery
# i przechodzi do następnej iteracji, bez wyświetlania samogłoski.
#
# 4. `print(letter)`:
# Jeśli litera nie jest samogłoską (nie spełnia warunków `if`),
# zostaje ona wyświetlona. Dla słowa "Gregory", tylko litery "G", "r", "g", "r" oraz "y"
# zostaną wyświetlone, ponieważ "e" i "o" są samogłoskami i są pomijane przez pętlę.
#
# 5. Pętla kontynuuje działanie dla każdej kolejnej litery w słowie "Gregory",
# sprawdzając, czy są one samogłoskami i wyświetlając je, jeśli nie są.
#
# 6. Po przejściu przez wszystkie litery w słowie, pętla się kończy.
#
# Wynikiem działania tego kodu dla słowa "Gregory"
# będzie wyświetlenie liter "G", "r", "g", "r" i "y", pomijając "e" i "o".
# ===============================================================================================================

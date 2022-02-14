# # -*- coding: utf-8 -*-
# """
# Created on Fri Jan 28 04:26:23 2022

# @author: mi
# """
print("\nUppgift 1\n")

"""Definiera en funktion som testar om elementen i en lista är sorterade"""


def is_sorted(my_list):
    n = len(my_list)
    if n <= 1:
        return True
    elif n > 1:
        for i in range(n):
            for j in range(i + 1, n):
                if my_list[j] < my_list[i]:
                    return False

        return True


print(is_sorted([1, 4, 23, 101, 2912]))
print(is_sorted([1, 4, 23, 2012, 101]))
print(is_sorted([]))
print(is_sorted([-1]))
print(is_sorted([2, 1, 4]))


"""Funktion som sätter in ett element x i en redan sorterad lista my_list"""


def insert_in_sorted(x, my_list):

    a = is_sorted(my_list)

    if a == True:
        my_list.append(x)
        l = len(my_list) - 1
        while l > 0:
            if my_list[l] < my_list[l - 1]:
                my_list[l], my_list[l - 1] = my_list[l - 1], my_list[l]
            l -= 1

        return my_list

    elif a == False:
        raise ValueError("Input list must be sorted.")


print(insert_in_sorted(2, []))
print(insert_in_sorted(2, [2, 2]))
print(insert_in_sorted(2, [0, 1, 2, 3, 4]))
print(insert_in_sorted(5, [0, 1, 3, 4]))
try:
    print(insert_in_sorted(5, [0, 1, 3, 2]))
except:
    print("heje wops")


"""Funktion som insättningssortering med hjälp av insert_in_sorted"""


def insertion_sort(my_list):

    out = []
    for i in my_list:
        insert_in_sorted(i, out)
        continue

    return out


print(insertion_sort([12, 4, 3, -1]))


print("\nUppgift 2\n")

"""Funktion som tar ett filnamn "f" som parameter och returnerar antalet ord i filen"""


def count_words(f):

    with open(f) as h:
        sum = 0
        for line in h:
            words = line.split()
            sum = len(words) + sum
        return sum


print(count_words("loremipsum.txt"))

print("\nUppgift 3\n")

"""Funktion som tar ett filnamn "f" som parameter 
och skriver ut till en ny fil "annotated.txt" med originaltext
radnummer (räknat från 0), totalt antal ord upp till och inklusive den raden
"""


def annotate(f):

    with open(f, "r") as h, open("annotate.txt", "w") as h_out:

        radnummer = 0
        sum_word = 0
        for line in h:

            words = line.rstrip("\n").split(" ")
            sum_word += len(words)
            radnummer += 1

            h_out.write(line.rstrip("\n") + " " + str(radnummer - 1) + " " + str(sum_word) + "\n")


print(annotate("loremipsum.txt"))


print("\nUppgift 4\n")
"""Funktion som tar ett filhandtag h och sparar radnummer som nycklar och rader som värden i en uppslagstabell. Funktionen ska sedan returnera uppslagstabellen
"""


def save_rows(h):
    collected_words = {}

    radnummer = 0
    for line in h:

        collected_words[radnummer] = line.rstrip("\n")
        radnummer += 1

    return collected_words


"""Program som Frågar användaren efter en fil, läser in filen i uppslagstabellen (med "save_rows")
Frågar användaren om att ge två koordinater för rad och kolumn
Skriver ut tecknet i filen på platsen för koordinaterna.
"""


f = input("which file do you want to read: ")
h = open(f)
f = save_rows(h)
print(f)

print('At any point type"exit" to quit')
while True:
    a = input("provide row: ")
    if a == "exit":
        break

    b = input("provide column: ")

    for k in f.keys():
        if int(a) >= len(f):
            print("out of bound")
            break

        elif k == int(a):
            letter = list(f[k])
            new_letter = [item.replace(" ", "Space") for item in letter]
            for l in range(len(new_letter)):
                if l == int(b):
                    print(new_letter[l])

                elif int(b) > len(new_letter) - 1:
                    print("out of bound")
                    break

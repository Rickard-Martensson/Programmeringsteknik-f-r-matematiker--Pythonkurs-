#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:28:24 2022

@author: rebeckaalgervik
"""

# Uppgift 1
"""a) Definiera en funktion som testar om elementen i en lista är
sorterade (dvs i ökande ordning):"""


def is_sorted(my_list):
    n = len(my_list)
    # när en lista har bara en element
    if n == 1:
        return True
    # när en lista har inte element
    if my_list == []:
        return True
    # Vi lekar efter om det är falskt i minskning ordning.
    for i in range(n - 1):
        if my_list[i] > my_list[i + 1]:
            return False
    return True


"""b) Skriv en funktion som sätter in ett element x i en redan
sorterad lista my_list."""


def insert_in_sorted(x, my_list):
    # testa om my_list är sorterad och lyft ValueError om den inte är det.
    if not is_sorted(my_list):
        raise ValueError("Input list must be sorted")
    if my_list == []:
        return [x]
    n = len(my_list)
    for i in range(n):
        if my_list[i] >= x:
            my_list.insert(i, x)
            return my_list
    my_list.append(x)
    return my_list


# c) Skriv insättningssortering med hjälp av insert_in_sorted:


def insertion_sort(my_list):
    out = []
    for x in my_list:
        out = insert_in_sorted(x, out)
    return out


# Uppgift 2
"""Skriv en funktion "count_words(f)" som tar ett filnamn "f"
som parameter och returnerar antalet ord i filen."""


def count_words(f):
    words = 0
    with open(f) as h:
        for line in h:
            words = words + len(line.split())
        return words


print(count_words("input.txt"))

# Uppgift 3
"""
  Skriv en funktion "annotate(f)" som tar ett filnamn "f" som
  parameter och skriver ut till en ny fil "annotated.txt" med
  originaltext, radnummer (räknat från 0), totalt antal ord upp
  till och inklusive den raden.
  """


def annotate(f):
    h_in = open(f, "r")
    h_out = open("output.txt", "w")
    radnummer = 0
    words = 0
    for line in h_in:  # loop through the file, line by line
        line = line.rstrip("\n")  # remove new line
        words = words + len(line.split())
        h_out.write(line + " " + str(radnummer) + " " + str(words) + "\n")
        radnummer = radnummer + 1
    h_out.close()
    h_in.close()


annotate("input.txt")

# Uppgift 4
"""a) Skriv en funktion "save_rows(h)" som tar ett filhandtag h och
sparar radnummer som nycklar och rader som värden i en uppslagstabell.
Funktionen ska sedan returnera uppslagstabellen."""


def save_rows(hinput):
    radnummer = 0
    d = {}
    for line in hinput:
        line = line.rstrip("\n")  # remove new line
        d[radnummer] = line
        radnummer = radnummer + 1
    return d


hinput = open("input.txt")
print(save_rows(hinput))

# b) Använd "save_rows(h)" för att skriva en kodsnutt.


def main():
    filename = input("Which file do you want to read? ")
    while True:
        if filename == "exit":
            return  # We use return to end the program
        with open(filename, "r") as h:
            # d is a dictionary where we can look up any row from the file
            d = save_rows(h)
        while True:
            row = input("provide row: ")
            if row == "exit":
                return
            row = int(row)

            row_max = len(d) - 1  # Highest row number
            if row > row_max:
                print("Row out of bounds")
            else:
                break
        while True:
            column = input("provide column: ")
            if column == "exit":
                return
            column = int(column)
            # line is the line from the file at the row the user asked for
            line = d[row]
            col_max = len(line) - 1  # Highest column number
            if column > col_max:
                print("Column out of bounds")
            else:
                break

        if line[column] == " ":
            print("Space")
        else:
            print(line[column])


if __name__ == "__main__":
    main()

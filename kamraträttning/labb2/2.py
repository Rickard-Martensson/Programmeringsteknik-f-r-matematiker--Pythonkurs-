#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 19:29:22 2022

@author: ---
"""

# uppgift 1

p = [3, 0, 0, 1]
q = [-1, 0, 1, 0, 1]


# uppgift 2


def poly_to_string(p_list):
    """
    Return a string with a nice readable version of the polynomial given in p_list.
    """
    terms = []
    degree = 0

    # Collect a list of terms

    if len(p_list) == 0:
        return 0  # tomma listan printar "0"

    if p_list[0] == 0:
        return 0  # listan med nollor printar "0"

    for coeff in p_list:

        if degree == 0 and coeff == 0:
            coeff == ""  # Termer med koefficient 0 skrivs inte ut.
        elif degree == 0:
            terms.append(str(coeff))
        elif degree == 1 and coeff == 0:
            coeff == ""  # Termer med koefficient 0 skrivs inte ut.
        elif degree == 1 and coeff == 1:
            coeff == ""  # Termer med koefficient 1 skrivs utan koefficient.
        elif degree >= 1 and coeff == 0:
            coeff == ""  # Termer med koefficient 0 skrivs inte ut.
        elif degree >= 1 and coeff == 1:
            terms.append(str("x^") + str(degree))  # Termer med koefficient 1 skrivs utan koefficient.
        else:
            term = str(coeff) + "x^" + str(degree)
            terms.append(term)
        degree += 1

    final_string = " + ".join(terms)  # The string ' + ' is used as "glue" between the elements in the string
    return final_string


# uppgift 3


# a)

p0 = [2, 0, 3, 0]
q0 = [0, 0, 0]


def leading_coefficient(p_list):
    new_list = p_list.copy()  # gör en kopia av listan
    while p_list:
        new_list.reverse()
        for degree, coeff in enumerate(new_list):
            if coeff != 0:
                return coeff
            else:
                return 0


# b)
def degree(p_list):
    new_list = p_list.copy()  # gör en kopia av listan
    while p_list:
        new_list.reverse()
        for degree, coeff in enumerate(new_list):
            if coeff != 0:
                return (len(p_list) - 1) - degree
            else:
                return 0


# uppgift 4
def eval_poly(coeff, x):
    pol = 0  # polynom är lika med noll
    for degree in range(len(coeff)):  # itererar över listan från 0 till längden av listan
        pol += coeff[degree] * x ** degree
    return pol


# uppgift 5
# a)


def neg_poly(p_list):
    neg_poly = []  # tom lista
    for coefficient in p_list:
        neg_poly.append(coefficient * -1)  # lägger till polynomet från p_list multiplicerad med -1
    return neg_poly


# b)
def add_poly(p_list, q_list):

    pol = []  # tom lista
    if len(p_list) <= len(q_list):
        for degree in range(len(p_list)):  # itererar över listan från 0 till längden av p_list
            pol.append(p_list[degree] + q_list[degree])  # adderar coeff av p_list och q_list baserade på degree/index, lägger de i pol listan
        for degree in range(len(p_list), len(q_list)):  # itererar över listan från längden av p_list till längden av q_list
            pol.append(q_list[degree])  # lägger coeff av q_list i pol listan
    elif len(p_list) > len(q_list):
        for degree in range(len(q_list)):  # itererar över listan från 0 till längden av q_list
            pol.append(p_list[degree] + q_list[degree])  # adderar coeff av p_list och q_list baserade på degree/index, lägger de i pol listan
        for degree in range(len(q_list), len(p_list)):  # itererar över listan från längden av q_list till längden av p_list
            pol.append(p_list[degree])  # lägger coeff av p_list i pol listan

    return pol


# c)


# c)
def sub_poly(p_list, q_list):

    pol = []  # tom lista
    if len(p_list) < len(q_list):
        for degree in range(len(p_list)):  # itererar över listan från 0 till längden av q_list
            pol.append(p_list[degree] - q_list[degree])  # coeff av p_list subtraheras av coeff av q_list baserade på degree/index, lägger de i pol listan
        for degree in range(len(p_list), len(q_list)):  # itererar över listan från längden av q_list till längden av p_list
            pol.append(-q_list[degree])  # lägger negativ coeff av q_list i pol listan
    elif len(p_list) > len(q_list):
        for degree in range(len(q_list)):  # itererar över listan från 0 till längden av p_list
            pol.append(p_list[degree] - q_list[degree])  # coeff av q_list subtraheras av coeff av p_list baserade på degree/index, lägger de i pol listan
        for degree in range(len(q_list), len(p_list)):  # itererar över listan från längden av p_list till längden av q_list
            pol.append(-p_list[degree])  # lägger negativ coeff av p_list i pol listan
    elif len(p_list) == len(q_list):
        return []

    return pol

    # d)


def eq_poly(p_list, q_list):
    if len(p_list) <= len(q_list):
        for degree in range(len(q_list)):
            if degree > len(p_list) - 1:
                if q_list[degree] != 0:
                    return False
            else:
                if q_list[degree] != p_list[degree]:
                    return False
        return True
    else:
        for degree in range(len(p_list)):
            if degree > len(q_list) - 1:
                if p_list[degree] != 0:
                    return False
            else:
                if q_list[degree] != p_list[degree]:
                    return False
        return True


print(poly_to_string(p))

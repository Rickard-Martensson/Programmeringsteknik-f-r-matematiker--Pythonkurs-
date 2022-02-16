#########lab4
from labb2 import *

#########uppgift 1a
def symbolic_derivative(p_list):

    derivative = list(p_list[i] * i for i in range(1, len(p_list)))

    return derivative


# #########uppgift 1b

p_fun = lambda x: eval_poly(p, x)
q_fun = lambda x: eval_poly(q, x)


def numeric_derivative(f, h):

    """
    returns the numerical derivative using lambda
    """

    return lambda x: (f(x + h) - f(x - h)) / (2 * h)


#########uppgift 2


def print_poly_from_file(f):

    """
    creates first a list with each line in it.
    then we split each line, and convert elements to integers
    then print with poly to string function
    """

    with open(f, "r") as file:

        lines = file.read().splitlines()

        for line in lines:
            poly = list(map(int, line.split(" ")))
            print(poly_to_string(poly))


#########uppgift 3

import numpy as np


######## a)
def mul_poly(p_list, q_list):

    """
    creates arrays from the lists
    uses polymul to multiplicate
    """

    p_array = np.array(p_list)
    q_array = np.array(q_list)

    poly = np.polymul(p_array, q_array)

    return poly.tolist()


######## b)


def coeff_product(p_list, q_list):

    """
    first some restructuring of the list
    creates arrays from the lists
    raises value errors if the arrays are still not of the sama lenghts
    then it uses np.multiply to multiply the lists
    """

    if p_list == []:
        return 0

    if q_list == []:
        return 0

    for i in p_list:
        if len(p_list) > 1:
            if p_list[-1] == 0:
                p_list.pop(-1)

    for i in q_list:
        if len(p_list) > 1:
            if q_list[-1] == 0:
                q_list.pop(-1)

    p_array = np.array(p_list)
    q_array = np.array(q_list)

    if len(p_array) != len(q_array):
        raise ValueError("the polynomials must have the same degree")

    else:
        return sum(np.multiply(p_list, q_list))

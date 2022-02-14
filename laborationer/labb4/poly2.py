import random
import numpy as np
from poly import *
import unittest


def symbolic_derivative(p_list):
    """Calculates the derivative of a polynomial symbolically in O(n) time.

    Args:
        p_list (list[number]): [a list containing ints or floats with size n]

    Returns:
        [list[number]]: [a list containing ints or floats with size n-1]

    Example:
        [3, 0, 0, 1] -> [0, 0, 3]
        [1] -> []
        [] -> []
    """
    return [x * idx for idx, x in enumerate(p_list)][1:]


def numeric_derivative(p_list, h):
    """Calculates the derivative of a polynomial numerically .

    Args:
        p_list (list[number]): [a list containing ints or floats with size n]
        h ([number]): [the limit, as h gets closer to 0 the evaluation goes to the correct value]

    Returns:
        [lambda]: [a lambda function that takes a x([number]) and returns the derivative at that point]

    Examples:
        numeric_derivative([0, 0, 1], 0.0001)(2) -> 4.000000000004
        derivative of x^2 evaluated at x=2, with a h= 0.0001 yields 4.000000000004, which is close to the correct value 4.
    """
    return lambda x: (eval_poly(p_list, x + h) - eval_poly(p_list, x - h)) / (2 * h)


def print_poly_from_file(filename):
    """Prints a polynom written in coefficient form to the command line.
    Treats each line as a seperate polynom

    Args:
        filename (string): a filename containing a polynom written in coefficient form

    Examples:
        -1000 -> -1000
        0 200 -> 200x
        -30 0 5 -> -30 + 5x^2
        -300 -300 0 1 -> -300 -300x + x^3
    """
    f = open(filename, "r")
    for line in f:
        print(poly_to_string(list(map(int, line.split()))))


def mul_poly(p, q):
    """multiplies two polynomials together, coefficient-wise

    Args:
        p (list[number]): a list containing ints or floats with size n
        q (list[number]): a list containing ints or floats with size n

    Returns:
        (list[number]): a list containing ints or floats with size n

    Example:
        [1, 2, 3], [2, 3, 4] -> [2, 7, 16, 17, 12]
    """
    return (np.polymul(np.array(p), np.array(q))).tolist()


def _get_degree(p):
    """
    Example:
    [0] -> 0
    [] -> 0
    [5] -> 0
    [5, 2] -> 1
    """
    return 0 if len(p) == 0 else len(p) - 1


def coeff_product(p, q):
    """calculates the cool thing

    Args:
        p_list (list[number]): a list containing ints or floats with size n
        q_list (list[number]): a list containing ints or floats with size n

    Returns:
        [number]: [the sum of the coefficients of the two lists]
    """
    p, q = drop_zeroes(p), drop_zeroes(q)
    if _get_degree(p) != _get_degree(p):
        raise ValueError(f"the polynomials are of degree { _get_degree(p)} and { _get_degree(p)}, but they need to be of the same degree")
    return 0 if p == [] or q == [] else sum([p[i] * q[i] for i in range(len(p))])


if __name__ == "__main__":
    p = [3, 0, 0, 1]
    q = [-1, 0, 1, 0, 1]
    # //===Uppgift 1====\\
    assert symbolic_derivative(p) == [0, 0, 3]
    assert symbolic_derivative(q) == [0, 2, 0, 4]
    assert symbolic_derivative([1]) == []
    assert symbolic_derivative([]) == []
    assert poly_to_string(symbolic_derivative(p)) == "3x^2"
    assert poly_to_string(symbolic_derivative(q)) == "2x + 4x^3"
    assert poly_to_string(symbolic_derivative([1])) == "0"
    assert poly_to_string(symbolic_derivative([])) == "0"

    for i in range(3):
        """loops trough a couple of random polynomials and prints the relative error"""
        rand_poly = [random.randint(-15, 15) for _ in range(random.randint(2, 15))]
        rand_eval_point = random.randint(-10, 10)
        symbolic_eval = eval_poly(symbolic_derivative(rand_poly), rand_eval_point)
        numeric_eval = numeric_derivative(rand_poly, 0.1)(rand_eval_point)
        # print(
        #     "numeric:  {:15.2f}".format(numeric_eval)
        #     + "\nsymbolic: {:15.2f}".format(symbolic_eval)
        #     + "\nerror:    {:15.10f}".format(abs(numeric_eval / symbolic_eval - 1))
        # )
    assert abs(numeric_derivative(p, 0.1)(0) - 0.01) < 0.1
    assert abs(numeric_derivative(p, 0.1)(1) - 3) < 0.1
    assert abs(numeric_derivative(q, 0.1)(2) - 36) < 0.1
    assert abs(numeric_derivative(q, 0.1)(-2) - (-36)) < 0.1

    # //===Uppgift 2====\\
    print_poly_from_file("polynom.txt")

    # //===Uppgift 3====\\
    print(mul_poly(p, q))
    assert mul_poly([1, 2, 3], [2, 3, 4]) == [2, 7, 16, 17, 12]
    assert mul_poly([], [2, 3, 4]) == [0, 0, 0]
    assert mul_poly([1, 2, 3], []) == [0, 0, 0]
    assert mul_poly([1, 2, 3], [-2, 4, 3, -17]) == [-2, 0, 5, 1, -25, -51]

    assert coeff_product([1, 2, 3], [2, 3, 4]) == 20
    assert coeff_product([1], [4]) == 4
    assert coeff_product([1, 2, 3, 0, 0], [4, 3, 2, 0]) == 16
    assert coeff_product([], [0]) == 0
    assert coeff_product([], [2]) == 0
    assert coeff_product([3], [0]) == 0
    try:
        coeff_product([1, 0, 1], [4, 0])
    except IndexError as E:
        print("seems to be working fine. Error:", E)
    except Exception as E:
        print("some other error occured;", E)
    print("passed all tests")

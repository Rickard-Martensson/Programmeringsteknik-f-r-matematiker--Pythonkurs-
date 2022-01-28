# Author: Rickard Mårtensson rmarte@kth.se
import math


def poly_to_string(p_list):
    """takes in a list with coefficients for a polynom, and returns a string representing the polynom

    Args:
        p_list ([list[number]]): [a list of numbers, ints or floats]

    Returns:
        [string]: [a string representing a polynomial]

    Example:
        [3, 2, 1, 0] -> 3 + 2x + 1x^2 + 0x^3
        [0, 2, 1, 0] -> 0 + 2x + 1x^2 + 0x^3
    """
    terms = []
    degree = 0

    # Collect a list of terms
    if all(e == 0 for e in p_list):
        return "0"

    for coeff in p_list:
        if degree == 0:
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + "x")
        else:
            term = str(coeff) + "x^" + str(degree)
            terms.append(term)
        degree += 1

    final_string = " + ".join(terms)
    return final_string


def eval_poly(p_list: list, x: float) -> float:
    """Evaluates the value of a polynomial p_list at x

    Args:
        p_list (list[number]): coefficients of a polynomial in the form of a list of numbers (ints of floats)
        x (number): location where polynomial should be evaluated. can be a int or float

    Returns:
        float: output parsed as a float

    Example:
    [3, 2, 1, 0], 3 -> 18.0
    """

    poly_val = 0
    for idx, val in enumerate(p_list):
        poly_val += val * math.pow(x, idx)
    return poly_val


def drop_zeroes(p_list):
    """Drops the trailing zeroes in a polynom in list-form

    Args:
        p_list ([list[numbers]]): list of integers or floats

    Returns:
        return_list ([list[numbers]]) : list of integers or floats

    Example:
        [4, 2, 0, 1, 0, 0, 0] -> [4, 2, 0, 1]
    """
    for i in reversed(p_list):
        if i == 0:
            p_list.pop()
        else:
            break
    return p_list


def neg_poly(p_list):
    """negates all terms in a polynom"""
    return list(map(lambda x: -1 * x, p_list))


def _pad_zeroes(p_list: list, zeroes: int):
    """pads zeros to the end of a list so that the total length of the list is zeroes long"""
    return p_list + [0] * (zeroes - len(p_list))


def add_poly(p_list: list, q_list: list) -> list:
    """adds two polynomials together

    Args:
        p_list ([type]): a list of floats or ints representing a polynom
        q_list ([type]): a list of floats or ints representing a polynom

    Returns:
        ([list[number]]): a list of floats or ints representing a polynom

    Example:
        [1,2,3], [3,2,1] -> [4, 4, 4]
    """
    max_len = max(len(p_list), len(q_list))
    return list(map(lambda x, y: x + y, _pad_zeroes(p_list, max_len), _pad_zeroes(q_list, max_len)))


def sub_poly(p_list, q_list):
    """subtracts two polynomials from each other, ie subtracts q_list from p_list

    Args:
        p_list ([type]): a list of floats or ints representing a polynom
        q_list ([type]): a list of floats or ints representing a polynom

    Returns:
        ([list[number]]): a list of floats or ints representing a polynom

    Example:
        [1,2,3], [3,2,1] -> [-2, 0, 2]
    """
    print(p_list, q_list, add_poly(p_list, neg_poly(q_list)))
    return add_poly(p_list, neg_poly(q_list))
    # return list(map(lambda x, y: x + y, p_list, neg_poly(q_list)))


def eq_poly(p_list, q_list):
    print("p", drop_zeroes(p_list), "q:", drop_zeroes(q_list))
    return drop_zeroes(p_list) == drop_zeroes(q_list)


def _test():
    p = [2, 0, 1]
    q = [-2, 1, 0, 0, 1]
    # uppgift 1
    assert poly_to_string([2, 1]) == "2 + 1x"
    # uppgift 2
    assert poly_to_string([0, 0, 0]) == "0"
    assert poly_to_string([]) == "0"
    # uppgift 3
    assert drop_zeroes([4, 2, 0, 1, 0, 0, 0]) == [4, 2, 0, 1]
    assert drop_zeroes([]) == []
    # uppgift 4
    assert eval_poly([1, 1, 1], 2) == 7.0
    # uppgift 5
    assert neg_poly([1, 2, 3]) == [-1, -2, -3]
    assert eq_poly(add_poly(p, q), add_poly(q, p))
    assert eq_poly(sub_poly(p, p), [])
    assert eq_poly(sub_poly(p, neg_poly(q)), add_poly(p, q))
    assert not eq_poly(add_poly(p, p), [])
    assert eq_poly(sub_poly(p, q), [4, -1, 1, 0, -1])
    assert eval_poly(add_poly(p, q), 12) == eval_poly(p, 12) + eval_poly(q, 12)
    # assert eval_poly([1, 1, 1])
    # assert poly_to_string([1, 2, ]3)


if __name__ == "__main__":
    _test()

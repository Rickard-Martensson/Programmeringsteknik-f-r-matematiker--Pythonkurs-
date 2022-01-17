# Author:
import math


def poly_to_string(p_list):
    """Function that takes a list and returns a polynom with
    constants of given list

    Args:
        p_list ([number]): list of integers or floats

    Returns:
        string : a string in the shape of a polynomial

    Example usage:
        [0, 0, 0] -> "0"
        [-2, 1, 0, 0, 1] -> ""
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

    final_string = " + ".join(terms)  # The string ' + ' is used as "glue" between the elements in the string
    return final_string


def eval_poly(p_list: list, x: float) -> float:
    """Evaluates the value of a polynomial p_list at x

    Args:
        p_list (list[number]): coefficients of a polynomial in the form of a list of numbers (ints of floats)
        x (number): location where polynomial should be evaluated. can be a int or float

    Returns:
        float: output parsed as a float
    """

    poly_val = 0
    for idx, val in enumerate(p_list):
        poly_val += val * math.pow(x, idx)
    return poly_val


def drop_zeroes(p_list):
    """Drops the trailing zeroes in a polynom

    Args:
        p_list ([numbers]): list of integers or floats

    Returns:
        return_list ([numbers]) : list of integers or floats
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
    """pads zeros to the end of a list so that the total length of the list is zeroes long

    Args:
        p_list (list[numbers]): list of integers or floats
        zeroes ([type]): length of the requested list

    Returns:
        list:
    """
    return p_list + [0] * (zeroes - len(p_list))


def add_poly(p_list: list, q_list: list) -> list:
    """adds two polynomials together

    Args:
        p_list ([type]): [description]
        q_list ([type]): [description]

    Returns:
        list:
    """
    max_len = max(len(p_list), len(q_list))
    return list(map(lambda x, y: x + y, _pad_zeroes(p_list, max_len), _pad_zeroes(q_list, max_len)))


def sub_poly(p_list, q_list):
    print(p_list, q_list, add_poly(p_list, neg_poly(q_list)))
    return add_poly(p_list, neg_poly(q_list))
    # return list(map(lambda x, y: x + y, p_list, neg_poly(q_list)))


def eq_poly(p_list, q_list):
    print("p", drop_zeroes(p_list), "q:", drop_zeroes(q_list))
    return drop_zeroes(p_list) == drop_zeroes(q_list)


def main():
    # Uppgift 1
    p = [2, 1]
    q = [-2, 1, 0, 0, 1]
    print("p:", poly_to_string(p), "q:", poly_to_string(q))

    print()


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
    main()
    _test()

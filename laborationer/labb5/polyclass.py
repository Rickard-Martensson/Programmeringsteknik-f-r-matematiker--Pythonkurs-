from __future__ import annotations
from typing import Type
import math


class Poly:
    def __init__(self, l: list[float] = None) -> None:
        """[summary]

        Args:
            list (list[float]): [a list of floats, each representing ]
        """
        if l == None:
            self.l = []
        elif not isinstance(l, list):
            l_type = type(l)
            raise TypeError(f'Wrong type. Expected "list", found {l_type}')
        self.l = l

    def degree(self) -> int:
        """Returns the degree of a polynomail

        Raises:
            ValueError: If the polynomial is the zero-polynomial

        Returns:
            int: the degree of the polynomial

        Examples:
            [0, 0, 1] -> 2
            [0, 3, 0, 1, 0] -> 3
            [0] -> ValueError
        """
        if self._is_zero_polynomial():
            raise ValueError(f"the zero polynomial does not have a degree")
        new_poly = self.drop_zeroes()
        return len(new_poly.l) - 1

    def _is_zero_polynomial(self) -> bool:
        if all(e == 0 for e in self.l):
            return True
        return False

    def evaluate(self, x: float) -> float:
        """Evaluates the value of a polynomial at x

        Args:
            p_list (list[number]): coefficients of a polynomial in the form ofa list of numbers (ints of floats)
            x (number): location where polynomial should be evaluated. can be a int or float

        Returns:
            float: output parsed as a float

        Example:
        [3, 2, 1, 0], 3 -> 18.0
        [0, 0, 1], 13 -> 169.0
        """
        poly_eval = 0
        for idx, val in enumerate(self.l):
            poly_eval += val * math.pow(x, idx)
        return poly_eval

    def __str__(self) -> str:
        terms = []

        if all(e == 0 for e in self.l):
            return "0"

        for idx, coeff in enumerate(self.l):
            if coeff == 0:
                continue
            if idx == 0:
                terms.append(str(coeff))
            elif idx == 1:
                terms.append(str(coeff) + "x")
            else:
                term = str(coeff) + "x^" + str(idx)
                terms.append(term)

        final_string = " + ".join(terms)
        return final_string

    def __repr__(self) -> str:
        return f"Poly({str(self.l)})"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Poly):
            return self.drop_zeroes() == __o.drop_zeroes()
        return False

    def __hash__(self) -> int:
        return hash(self.l)

    def _pad_zeroes(self, zeroes: int):
        """pads zero-coefficients at to the end of a Polynomial so that the total length of the list is zeroes long"""
        return Poly(self.l + [0] * (zeroes - len(self.l)))

    def __add__(self, __o) -> Poly:
        """adds two polynomials together"""
        if not isinstance(__o, Poly):
            raise TypeError(f"expected Poly type, found {type(__o)}")

        max_len = max(len(self), len(__o))
        return list(map(lambda x, y: x + y, self._pad_zeroes(max_len), __o._pad_zeroes(max_len)))

    def __neg__(self) -> Poly:
        """Negates every coefficient in a polynomial"""
        return Poly(list(map(lambda x: -1 * x, self.l)))

    def __sub__(self, __o) -> Poly:
        return self + (-__o)

    def __mul__(self, __o) -> Poly:
        """Todo: fast polynomial multiplication using fast fourier transform. Complexity: O(n log n)"""
        # source: https://www.youtube.com/watch?v=h7apO7q16V0
        pass

    def drop_zeroes(self):
        """drops trailing zeroes of a polynom"""
        for i in reversed(self.l):
            if i == 0:
                self.l.pop()
            else:
                break
        return Poly(self.l)


# poly_a = Poly([1, 3, 2])
# poly_a = Poly(1)
# poly_a = Poly([1, 3, 2])

print(repr(Poly([1, 2, 3])))
print(Poly([1, 2, 3]))

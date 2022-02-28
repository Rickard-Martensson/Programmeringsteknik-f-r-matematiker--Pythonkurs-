from __future__ import annotations
from typing import Type
import matplotlib.pyplot as plt


class Poly:
    def __init__(self, l: list[float] = None) -> None:
        """
        A class used for calculations with polynomials.
        Polynomials are initiated and stored as a list of numbers
        Will default to the zero-polynomial if there is no imput-list

        Args:
            list (list[float]): [a list of floats, each representing a coefficient in the polynomial]

        Example usage:
            Poly([1, 2, 3]) -> 3x^2 + 2x + 1

        Raises:
            Valueerror: l is neither a list of numbers, nor un-set.
        """
        if l == None:
            self.l = []
        elif not isinstance(l, list):
            l_type = type(l)
            raise TypeError(f'Wrong type. Expected "list", found {l_type}')
        elif len(l) != 0:
            if (not isinstance(l[0], float)) and (not isinstance(l[0], int)):
                raise TypeError(f"Wrong type. Expected list of floats or ints, found list of {type(l[0])}")
        self.l = l

    def plot_poly(self, filename: str = "myplot", x_start: float = -10, x_end: float = 10, colour: str = "b", step_size: float = 1) -> None:
        """Plots a polynomial from x_start to x_end, with steps step_size

        Args:
            filename (str, optional): _description_. Defaults to "myplot".
            x_start (float, optional): _description_. Defaults to -10.
            x_end (float, optional): _description_. Defaults to 10.
            color (str, optional): _description_. Defaults to "b".

        Returns:
            Nothing, but creates a file named 'filename' with the plot

        Examples:
            Poly([3, -1, 2, 1]).plot_polt() -->

            y
            |            /
            |    _______/
            |   /
            |  /
            |_________________x
        """
        plt.plot([x for x in range(x_start, x_end + step_size, step_size)], [self.evaluate(x) for x in range(x_start, x_end + step_size, step_size)], color=colour)
        plt.savefig(filename)

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
            poly_eval += val * x**idx
        return poly_eval

    def __str__(self) -> str:
        terms = []

        if all(e == 0 for e in self.l):
            return "0"

        for idx, coeff in enumerate(self.l):
            if coeff == 0:
                continue
            str_coeff = "" if coeff == 1 else str(coeff)
            if idx == 0:
                terms.append(str_coeff)
            elif idx == 1:
                terms.append(str_coeff + "x")
            else:
                term = str_coeff + "x^" + str(idx)
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


hej = Poly()


class QPoly(Poly):
    def __init__(self, l: list[float] = None) -> None:
        super().__init__(l)
        if l == None:
            self.l = [0, 0, 1]
        self = self.drop_zeroes()
        if len(l) != 3:
            raise ValueError(f"not a quadratic polynomial. Expected list of length 3, found length {len(l)}")

    def compute_roots(self) -> list[float]:
        """Computes the roots to a quadratic polynomial. Will calculate complex roots aswell.

        Returns:
            list[float]: A list of length 1 or 2, each element being a root.

        Examples:
            QPoly([1, 4, 4]).compute_roots(self) --> [-0.5]
            QPoly([10, 4, 2]).compute_roots(self) --> [(-1 - 2j), (-1 + 2j)]

        """
        c, b, a = self.l
        root = (b**2 - 4 * a * c) ** 0.5 if (b**2 >= 4 * a * c) else complex(0, ((4 * a * c - b**2)) ** 0.5)
        return [(-b - root) / (2 * a), (-b + root) / (2 * a)] if root != 0 else [-b / (2 * a)]


def test():
    # del 1
    p0 = Poly([0, 1])
    p1 = Poly([0, 0, 0, 0, 1, 0])
    p2 = Poly([0, 0, 4, 5])
    p3 = Poly([5, 4, 3, 2, 1])
    assert p0.degree() == 1
    assert p1.degree() == 4
    assert p2.degree() == 3
    assert p3.degree() == 4
    assert p0.evaluate(7) == 7
    assert p1.evaluate(1) == 1
    assert p1.evaluate(2) == 16
    assert p2.evaluate(0) == 0
    assert p2.evaluate(1) == 9
    assert p2.evaluate(2) == 56
    assert p3.evaluate(1) == 15

    # del 2
    assert str(p0) == "x"
    assert str(p1) == "x^4"
    assert str(p2) == "4x^2 + 5x^3"
    assert str(p3) == "5 + 4x + 3x^2 + 2x^3 + x^4"

    # del 3
    qp1 = QPoly([1, 4, 4])
    qp2 = QPoly([-16, 0, 1])
    qp3 = QPoly([10, 4, 2])
    assert qp1.compute_roots() == [-0.5]
    assert qp2.compute_roots() == [-4, 4]
    assert qp3.compute_roots() == [(-1 - 2j), (-1 + 2j)]
    try:
        QPoly([1, 4, 4, 4, 6])
    except ValueError as E:
        print(f'seems to be working, caught error "{E}"')

    # del 4
    p = Poly([3, -1, 2, 1])
    p.plot_poly("myplot")


if __name__ == "__main__":
    test()

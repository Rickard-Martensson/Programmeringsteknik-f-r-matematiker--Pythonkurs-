from typing import List
import operator

# http://www.math.bas.bg/bantchev/place/rpn/rpn.python.html
ASERTS = []


class Påstående:
    def __init__(self, name) -> None:

        self.name = name
        self.b = False

    def __str__(self) -> str:
        _str = "T" if self.b else "F"
        return f"{self.name}:{self.b}"


class Operator:
    def __init__(self, type) -> None:
        self.type = "And"

    def __str__(self) -> str:
        return "^"

    def __eq__(self, __o: object) -> bool:
        return self.type == __o.type


class Solver:
    def __init__(self, l: list) -> None:
        self.l = l
        pass

    def solve(self):
        symbols = [Påstående("p"), Påstående("q"), Påstående("r"), Påstående("s")]
        for i in range(2 ** len(symbols)):
            for j in symbols:
                print("ye")


"""

[p, q, &, r &]

A = p
B = Q
OP = & -> A 

"""


def getBoolAtPosX(Number, x):
    """tolkar Number som ett binärt tal, och returnerar siffran på den x:e positionen, räknat bakifrån

    Args:
        Number (int): ett stort tal
        x (int): ett tal

    Returns:
        int: 0 or 1

    Example:
        1, 0    -> 1
        2, 0    -> 0
        2, 1    -> 1
        8, 3    -> 1
        4112, 4 -> 1
        5, 9    -> 0
        # same examples again, but written in binary
        1, 0             -> 1
        10, 0            -> 0
        10, 1            -> 1
        1000, 3          -> 1
        1000000010000, 4 -> 1
        000000101, 9     -> 0
    """
    return (Number >> x) & 1
    #     return True
    # return False


# a = Påstående()
# b = Operator("^")
# c = Påstående()
# listan = [a, b, c]

# lösare = Solver(listan)
# lösare.solve()


def satslösare():

    return True


def main():
    a = 6
    b = 5
    print(a, b, getBoolAtPosX(a, b))
    # while True:
    #     indata = input("[P]rint truth table \n[A]dd assertion \n[R]emove assertion \n[Q]uit.")
    #     if indata == "A":
    #         text = input("Skriv in några påståenden").split()
    minsolver = Solver("hej")
    minsolver.solve()


main()

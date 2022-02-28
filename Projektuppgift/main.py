from typing import List
import operator
from termcolor import color

from numpy import isin

# http://www.math.bas.bg/bantchev/place/rpn/rpn.python.html
ASERTS = []


class Bol:
    def __init__(self, name, b=False) -> None:

        self.name = name
        self.b = b

    def __str__(self) -> str:
        _str = "T" if self.b else "F"
        return f"{self.name}({_str})"

    def __repr__(self) -> str:
        _str = "T" if self.b else "F"
        return f"{self.name}({_str})"


class Ops:
    def __init__(self, typ) -> None:
        self.typ = typ

    def __str__(self) -> str:
        return f"Op({self.typ})"

    def __repr__(self) -> str:
        return f"Op({self.typ})"

    def __eq__(self, __o: object) -> bool:
        return self.type == __o.type

    def type(self):
        return self.typ


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


def tolka(v_list, tal):
    current_eval = 0
    påstående_längd = len(v_list)
    bool_list = [getBoolAtPosX(tal, x) for x in range(påstående_längd)]
    print(bool_list, end="")


"""
def RPNtolk(sträng) -> bool:
    operators = ["AND", "OR"]
    stack = []
    for o in sträng:
        if o in operators:
            op1 = stack.pop(0)
            op2 = stack.pop(0)
            print(op1)
            calc = op1 * op2
            stack.append(calc)
        else:
            if o == "t":
                stack.append(1)
            else:
                stack.append(0)
    print(stack)


RPNtolk(["t", "t", "AND"])
"""


def calcNot(bol1):
    return Bol("x", not bol1.b)


def calc(bol1, op, bol2=None):
    if not isinstance(bol1, Bol):
        raise ValueError("wrong type :(")
    if not isinstance(bol2, Bol):
        raise ValueError("wrong type :(")
    if isinstance(op, Ops):
        if op.typ == "and":
            return Bol("x", bol1.b and bol2.b)
        elif op.typ == "or":
            return Bol("x", bol1.b or bol2.b)


def RPNtolk(sträng) -> bool:
    stack = []
    for o in sträng:
        # print(o, end=" ")
        if isinstance(o, Ops):
            if o.type() == "not":
                bol1 = stack.pop(0)
                result = calcNot(bol1)
                stack.append(result)
            else:
                bol1 = stack.pop(0)
                bol2 = stack.pop(0)
                result = calc(bol1, o, bol2)
                stack.append(result)
        elif isinstance(o, Bol):
            stack.append(o)
        else:
            raise ValueError("list contains something that neither an operator nor operand")
    print(stack)


def main3():
    minLista = [Bol("p", False), Ops("not"), Bol("q", True), Ops("and")]

    bol_count = sum(isinstance(o, Bol) for o in minLista)

    for bin_comb in range(2**bol_count):
        local_list = []
        idx = 0
        for o in minLista:
            if isinstance(o, Ops):
                local_list.append(o)
            elif isinstance(o, Bol):
                newBol = Bol(o.name, getBoolAtPosX(bin_comb, idx))
                local_list.append(newBol)
                idx += 1
        print(local_list, end="")
        print(RPNtolk(local_list))


main3()
exit()


def main2():
    indata = input("Skriv en formel:").split()
    t_list = []
    v_list = []
    for c in indata:
        if c == "^":
            t_list.append(Operator("and"))
        else:
            v_list.append(Påstående(c))
            t_list.append(Påstående(c))

    # nu händer det grejjer

    for v in v_list:
        print(v.name, end=" ")
    print("")
    for tal in range(2 ** len(v_list)):
        for x in range(len(v_list)):
            print(f"{getBoolAtPosX(tal, x)}", end=" ")
        tolka2(t_list, tal)
        print("")


main2()

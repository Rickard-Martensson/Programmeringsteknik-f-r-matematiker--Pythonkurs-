def parens(p1, p2, s):
    if p1 < p2:
        return "(" + s + ")"
    else:
        return s


class Expr:
    prec = 1000


class Var(Expr):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class BinOp(Expr):
    def __init__(self, left, right):
        self._left = left
        self._right = right


class Plus(BinOp):
    prec = 1

    def __str__(self):
        s1 = parens(self._left.prec, self.prec, str(self._left))
        s2 = parens(self._right.prec, self.prec, str(self._right))
        return s1 + " + " + s2


class Times(BinOp):
    prec = 2

    def __str__(self):
        s1 = parens(self._left.prec, self.prec, str(self._left))
        s2 = parens(self._right.prec, self.prec, str(self._right))
        return s1 + " * " + s2


def parse(expr_string):
    """Parse a string in RPN into an expression"""
    # Mapping from strings to operators. Each entry is a
    # tuple of the operator constructor and its arity (number
    # of arguments it takes)
    operators = {"+": (Plus, 2), "*": (Times, 2)}
    stack = []
    for token in expr_string.split():
        if token in operators:
            op, arity = operators[token]
            if len(stack) < arity:
                raise ValueError("Not enough arguments to " + token)
            elif arity == 0:
                stack.append(op())
            else:
                args = stack[-arity:]
                stack = stack[:-arity]
                # apply op to the arguments in the list args, "unpacked"
                # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
                stack.append(op(*args))
        else:
            # All other strings are treated as variables
            stack.append(Var(token))
    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Not a valid expression: " + expr_string)


print(parse("5 7 + 9 *"))

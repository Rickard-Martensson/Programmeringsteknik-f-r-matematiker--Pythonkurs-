#  Uppgift 1: To define polynomial p and q.


p = [3, 0, 0, 1]
q = [-1, 0, 1, 0, 1]

# Define a function
def poly_to_string(p_list):
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if degree == 0:  # Evaluate different options
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + "x")
        else:
            term = str(coeff) + "x^" + str(degree)
            terms.append(term)
        degree += 1
    final_string = " + ".join(terms)
    return final_string


print(poly_to_string(p))  # Call for result
print(poly_to_string(q))


# Uppgift 2: To write a polynomial funktion without 0 and 1 coeffiecients


p = [3, 0, 0, 1]
q = [-1, 0, 1, 0, 1]

# Define a function
def poly_to_string(q_list):
    """
    Return a string with a nice readable version of the polynomial given in p_list.
    """
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in q_list:
        if degree == 0:  # Evaluate different options
            if coeff != 0:
                terms.append(str(coeff))
            else:
                """"""
        elif degree == 1:
            if coeff != 0:
                terms.append(+"x")
            else:
                """"""
        else:
            if coeff == 0:
                """"""
            else:
                term = str(coeff) + "x^" + str(degree)
                terms.append(term)
        degree += 1

    final_string = " + ".join(terms)
    return final_string


print("poly to string", poly_to_string(q))  # Call for result


#   Uppgift 3

# a) To write a polynomial function leading coeffieient

p = [3, 0, 0, 1]
q = [-1, 0, 1, 0, 1]
s = []
r = [0, 0, 0]

# Define a function
def leading_coefficient(q_list):

    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in q_list:
        if degree == 0:  # Evaluate different options
            if coeff == 0:
                """"""
            else:
                terms.append(str(coeff))
        elif degree == 1:
            if coeff == 0:
                """"""
            elif coeff == 1:
                term = terms.append("x")
                terms.append(term)
            else:
                term = terms.append(str(coeff) + "x")
                terms.append(term)
        else:
            if coeff == 0:
                """"""
            elif coeff == 1:
                term = "x^" + (str(degree))
                terms.append(term)
            else:
                term = str(coeff) + "x^" + (str(degree))
                terms.append(term)
        degree += 1
    final_string = " + ".join(terms)
    return final_string


print("leading coefficient", leading_coefficient(q)[-1])  # Call for result


# b) A program that gives the degree of a polynomial function

p = [3, 0, 0, 1]
q = [-1, 0, 1, 0, 1]
p0 = [2, 0, 3, 0]
q0 = [0, 0, 0]

# Define a function
def degree(q_list):
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in q_list:
        if degree == 0:  # Evaluate different options
            if coeff == 0:
                """"""
            else:
                terms.append(str(coeff))
        elif degree == 1:
            if coeff == 0:
                """"""
            elif coeff == 1:
                term = terms.append("x")
                terms.append(term)
            else:
                term = terms.append(str(coeff) + "x")
                terms.append(term)
        else:
            if coeff == 0:
                """"""
            elif coeff == 1:
                term = "x^" + (str(degree))
                terms.append(term)
            else:
                term = str(coeff) + "x^" + (str(degree))
                terms.append(term)
        degree += 1
    final_string = " + ".join(terms)
    return final_string


print("degree", degree(q)[-1])  # Call for result


#  Uppgift 4: To write a program that solve polynomial equations.

p = [3, 0, 0, 1]
q = [-1, 0, 1, 0, 10]
x = [2]

# Define a function
def eval_poly(p_list, x):
    coeff = []
    sum = 0
    grad = 0

    for coeff in p_list:
        if grad == 0:  # Evaluate different options
            sum = coeff
        else:
            sum += coeff * (x ** grad)
            grad += 1

    return sum


print("sum", sum(p))
print("eval", eval_poly(p, x))  # Call for result


# Uppgift 5

#  a) To write a polynomial equation that negate a polynomial.

p = [3, 0, 0, 1]
q = [-1, 0, 1, 0, 1]
Q = []
r = [0, 0, 0]

# Define a function
def neg_poly(q_list):
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in q_list:
        if degree == 0:  # Evaluate different options
            if coeff == 0:
                """"""
            else:
                terms.append(str(-coeff))
        elif degree == 1:
            if coeff == 0:
                """"""
            else:
                terms.append(str(coeff) + "x")
        else:
            if coeff == 0:
                """"""
            elif coeff == 1:
                term = "x^" + (str(degree))
                terms.append(term)
            else:
                term = str(coeff) + "x^" + (str(degree))
                terms.append(term)
        degree += 1
    final_string = " - ".join(terms)
    return final_string


print("neg poly", neg_poly(q))  # Call for result


#  b) To write a polynomial addition program

p = [3, 0, 0, 1, 0]
q = [-1, 0, 1, 0, 1]

# Define a function
def add_poly(p_list, q_list):
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff_p in p_list:
        if degree == 0:  # Evaluate different options
            for coeff_q in q_list:
                if coeff_p == 0 and coeff_q == 0:
                    """"""
                else:
                    terms.append(str(coeff_p))
                    terms.append(str(coeff_q))
        elif degree == 1:
            for coeff_q in q_list:
                if coeff_p == 0 and coeff_q == 0:
                    """"""
                else:
                    term_p = "x" + (str(degree))
                    terms.append(term_p)
                    term_q = "x" + (str(degree))
                    terms.append(term_q)
        else:
            for coeff_q in q_list:
                if coeff_q == 0 and coeff_p == 0:
                    """"""
                else:
                    term_p = str(coeff_p) + "x^" + (str(degree))
                    terms.append(term_p)
                    term_q = str(coeff_q) + "x^" + (str(degree))
                    terms.append(term_q)
                    degree += 1
    final_string = "+".join(terms)
    return final_string


print("add poly", add_poly(p, q))  # Call for result


# c) To write a polynomial subtraction program

p = [3, 0, 0, 1, 0]
q = [-1, 0, 1, 0, 1]

# Define a function
def sub_poly(p_list, q_list):
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff_p in p_list:
        if degree == 0:  # Evaluate different options
            for coeff_q in q_list:
                if coeff_p == 0 and coeff_q == 0:
                    """"""
                else:
                    terms.append(str(coeff_p))
                    terms.append(str(coeff_q))
        elif degree == 1:
            for coeff_q in q_list:
                if coeff_p == 0 and coeff_q == 0:
                    """"""
                else:
                    term_p = "x" + (str(degree))
                    terms.append(term_p)
                    term_q = "x" + (str(degree))
                    terms.append(term_q)
        else:
            for coeff_q in q_list:
                if coeff_q == 0 and coeff_p == 0:
                    """"""
                else:
                    term_p = str(coeff_p) + "x^" + (str(degree))
                    terms.append(term_p)
                    term_q = "-", str(coeff_q) + "x^" + (str(degree))
                    terms.append(term_q)
                    degree += 1
    final_string = "-".join(terms)
    return final_string


print("sub poly", sub_poly(p, q))  # Call for result


#  d) To write a program that determine equal polynomials.

p = [3, 0, 0, 1, 0]
q = [-1, 0, 1, 0, 1]

# Define a function
def eq_poly(p_list, q_list):
    terms = []
    degree = 0
    p, q = 0, 1

    # Collect a list of terms
    for coeff_p in p_list:
        if degree == 0:  # Evaluate different options
            for coeff_q in q_list:
                if coeff_p == coeff_q:
                    """"""
                else:
                    break
        elif degree == 1:
            for coeff_q in q_list:
                if coeff_p == coeff_q:
                    """"""
                else:
                    break
        else:
            for coeff_q in q_list:
                if coeff_q == coeff_p:
                    """"""
                else:
                    break
        return


print("eq poly", eq_poly(p, q))  # Call for result

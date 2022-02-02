""" Uppgift 1 """

p = [3, 0, 0, 1]
q = [-1, 0, 1, 0, 1]


def poly_to_string(p_list):
    """
    Return a string with a nice readable version of the polynomial given in p_list.
    """
    terms = []
    degree = 0

    # Collect a list of terms
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


poly_to_string(p)  # Testar funktionen
poly_to_string(q)

""" Uppgift 1 end """


"""#Uppgift 2"""

z = [0, 1, 1, 2, 0, 0]
w = []
y = [0, 0, 0]


def poly_to_string_v2(p_list):
    """
    Return a string with a nice readable version of the polynomial given in p_list.
    """
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if degree == 0:
            terms.append(str(coeff))
            if coeff == 0:  # if sats som kollar om värdet vi lagrade är 0
                terms.pop()  # tar bort elementet

        elif degree == 1:
            terms.append(str(coeff))
            if coeff == 1:  # if sats som kollar om värdet vi lagrade är 1
                terms.pop()  # tar bort elementet och
                terms.append("x")  # lägger till x
            elif coeff == 0:  # if sats som kollar om värdet vi lagrade är 0
                terms.pop()  # tar bort elementet
        else:
            terms.append(str(coeff))
            if coeff == 1:  # if sats som kollar om värdet vi lagrade är 1
                terms.pop()  # tar bort elementet
                terms.append("x^" + str(degree))  # lägger till x^degree
            elif coeff == 0:  # if sats som kollar om värdet vi lagrade är 0
                terms.pop()  # tar bort elementet
            else:
                terms.pop()
                term = str(coeff) + "x^" + str(degree)
                terms.append(term)
        degree += 1

    final_string = " + ".join(terms)  # The string ' + ' is used as "glue" between the elements in the string
    if terms == []:  # Kollar om listan är tom
        return 0  # skriver ut 0
    else:
        return final_string


poly_to_string_v2(p)  # Testar funktionen
poly_to_string_v2(q)
poly_to_string_v2(w)
poly_to_string_v2(y)

""" Uppgift 2 end """


"""
Uppgift 3a

Skriv en funktion som för ett icke-konstant polynom returnerar den 
högsta noll-skillda koefficienten (dvs termen med högst grad i polynomet) och 
för konstanta polynom returnerar konstanten:

"""

p0 = [2, 0, 3, 0]
q0 = [0, 0, 0]


def leading_coefficient(p_list):
    coeff = 0
    n = len(p_list)  # Tar längden på listan och sparar i variabeln n
    for i in range(n, 0, -1):  # lopp som går från sista elementet till första i listan
        if p_list[i - 1] != 0:  # letar efter tal skilda från 0
            coeff = p_list[i - 1]  # lagrar värdet i variablen coeff
            break  # avbryter loopen
        else:
            p_list.pop()  # tar bort sista elementet.

    return "Högsta koefficienten:", coeff  # Skriver ut resultatet


leading_coefficient(p)  # Testar funktionen
leading_coefficient(p0)
leading_coefficient(q0)

"""
Uppgift 3a end
 
"""


"""
Uppgift 3b 

Skriv en funktion som returnerar graden 
för ett polynom. Graden för ett konstant polynom är 0:
    
"""

p1 = [1, 0, 0, 1, 2, 0, 0, 0, 8, 0]
q1 = [1]


def degree(p_list):  # Samma funktion som 3a men ger graden som resultat
    grad = 0
    n = len(p_list)
    for i in range(n, 0, -1):
        if p_list[i - 1] != 0:
            grad = i - 1
            break
        else:
            p_list.pop()

    return "Graden på polynomet är:", grad


print("degree", degree(p))  # testar funktionen)
print("degree", degree(q))
print("degree", degree(p0))
print("degree", degree(q0))

""" Uppgift 3b end """

"""
Uppgift 4

Skriv en funktion som tar ett polynom och ett värde på 
variabeln x och returnerar polynomets värde i punkten x.

"""


def eval_poly(p_list, x):
    summa = 0  # tom lista
    n = len(p_list)  # ger längden på input-listan, används i forsatsen
    for i in range(0, n):
        summa = summa + (p_list[i] * x ** i)  # adderar summan och
    return summa


print("eval poly", eval_poly(p, 0))  # testar funktionen)
print("eval poly", eval_poly(p, 1))
print("eval poly", eval_poly(p, 2))
print("eval poly", eval_poly(q, 2))
print("eval poly", eval_poly(q, -2))

""" Uppgift 4 end """


"""Uppgift 5a Definiera negation av polynom:"""


def neg_poly(p_list):
    n = len(p_list)
    lista = []

    for i in range(0, n):
        lista.append(p_list[i] * -1)  # Multiplikation med -1 på alla element i listan
    return lista


neg_poly(p)  # testar funktionen

""" Uppgift 5a end """


"""Uppgift 5b Definiera addition av polynom:"""


def add_poly(p_list, q_list):
    n = len(p_list)  # längd lista 1
    m = len(q_list)  # längd lista 2
    summa = []  # tom lista

    if n > m:  # letar efter den längsta listan.
        a = n  # variablen a används i kommande for-loop.
        for i in range(0, n - m):
            q_list.append(0)  # fyller den kortaste listan med nollor tills listorna blir lika långa.
    elif m > n:
        a = m
        for i in range(0, m - n):
            p_list.append(0)
    else:
        a = n

    for i in range(0, a):
        summa.append(p_list[i] + q_list[i])  # adderar listorna.

    return summa


add_poly(p, q)  # testar funktionen.

""" Uppgift 5b end """


"""Uppgift 5c Definiera subtraktion av polynom: """

p2 = [1, 3, 4, 4]
q2 = [1, 2, 3, 4, 5]


def sub_poly(p_list, q_list):  # Samma funktion som 5b
    n = len(p_list)  # fast q_list multipliceras med -1 innan addition med p_list.
    m = len(q_list)
    summa = []

    if n > m:
        a = n
        for i in range(0, n - m):
            q_list.append(0)
    elif m > n:
        a = m
        for i in range(0, m - n):
            p_list.append(0)
    else:
        a = n

    for i in range(0, a):
        summa.append(p_list[i] + (-1 * q_list[i]))  #

    return summa


sub_poly(p2, q2)  # testar funktionen.

""" Uppgift 5c end """

""" Uppgift 5d Definiera en funktion som testar om två polynom är lika:"""

t = [1, 0]
t2 = [1, 1]


def eq_poly(p_list, q_list):
    n = len(p_list)  # längd lista 1
    m = len(q_list)  # längd lista 2
    summa = []  # tom lista
    kontroll = True

    if n > m:  # Likt 5a och 5b så är den här delen
        a = n  # till för att listorna ska bli lika långa.
        for i in range(0, n - m):
            q_list.append(0)
    elif m > n:
        a = m
        for i in range(0, m - n):
            p_list.append(0)
    else:
        a = n

    for i in range(0, a):
        summa.append(p_list[i] + (-1 * q_list[i]))  # lista 1 minus lista 2, sparar resultat i summa

    for i in range(0, a):
        if summa[i] != 0:  # söker igenom alla element i listan
            kontroll = False  # False om inte alla element i listan är noll
            break
        else:
            kontroll = kontroll
    return kontroll


eq_poly(t, t2)  # testar funktionen

""" Uppgift 5d end """

lista_a = [1, 3, 5, 7, 9]
lista_b = [2, 4, 6, 8, 10, 12, 14]


längsta_lista = max(len(lista_a), len(lista_b))
""" Vi räknar ut hur lång den längsta av båda listorna är.
len(lista_a) säger hur lång listan är.
max(X, Y) kommer att välja det största värdet av X och Y.
om vi bara loopa len(lista_a) gånger, alltså 5 gånger, så skulle de två sista värdena på b [12,14] inte komma med i vår slutgiltiga lista:(
"""
lista_summa = []
"""Vi skapar en tom lista som vi sen kan fylla med summan av lista_a och lista_b alltefterssom
"""

for i in range(längsta_lista):
    """Dehär är en for-loop, den kommer loopa över alla värden från 0 till (men inte till och med) 'längsta_lista'.
    Den kommer alltså att köra koden här under flera gånger. först kommer den låta i=0, nästa gång så kommer i=1, sen i=2 osv...add()
    """
    summa_pos_i = 0
    if len(lista_a) > i:
        """här kollar vi att lista_a faktiskt har ett värde på den i:te positionen.
        Programmet skulle crasha ifall vi skrev 'lista_a[5]' eller 'lista_a[6]' efterssom att lista_a bara har ett värde på position 0, 1, 2, 3, 4.add()
        Tex så är lista_a[3] = 7
        """
        summa_pos_i += lista_a[i]
    if len(lista_b) > i:
        """här gör vi samma test på lista_b, av samma anledning.
        i just dehär fallet så behöver vi ju inte det, men det kan ju vara så att lista_a skulle vara längre än lista_b.
        """
        summa_pos_i += lista_b[i]
    lista_summa.append(summa_pos_i)  # lägger ihop summan av båda listorna på position 'i', och lägger till den i vår summa-lista

print(lista_summa)

"""



Sen måste ju dom också tycka att det är en bra matching såklart



 i london på måndag. London är jäkligt fett, men jobbet handlar om android och kan typ inget om det.kanske 7/10, men det finns ju coolare saker att göra där borta. Men vet inte heller hur många offers man får
    

    """


from http.cookiejar import Cookie
from typing import List


def _binary_search(V: List[int], items: List[int], low: int, high: int, needle: int) -> int:
    if (low + 1) == high:
        return high
    pivot = (low + high) // 2
    if items[V[pivot]] < needle:
        low = pivot
    elif items[V[pivot]] > needle:
        high = pivot
    else:
        return pivot
    return _binary_search(V, items, low, high, needle)


def lis(items: List[int]) -> List[int]:
    inf = max(items) + 1
    P = [None] * len(items)  # where the number at index k points.
    V = [inf] * (len(items) + 1)  # last digit in the best subsequence with length k
    longest_seq_found = 0

    for i, item in items:
        v_index = _binary_search(V, items, 0, longest_seq_found + 1, item)
        V[v_index] = i
        P[i] = V[v_index - 1]
        longest_seq_found = max(longest_seq_found, v_index)

    output, prev_index = [], V[longest_seq_found]
    for _ in range(longest_seq_found):
        output.append(prev_index)
        prev_index = P[prev_index]

    output.reverse()
    return output


if Cookie.accept:
    collect_data()
else:
    collect_data()

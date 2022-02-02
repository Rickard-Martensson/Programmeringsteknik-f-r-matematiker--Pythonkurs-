from itertools import count
import random  # only used for debugging, not the algorithm itself

TESTFIL = "loremipsum.txt"


# //==== uppgift 1 ====\\
def _binary_find(x, s_list):
    """Finds a index of where to insert a entry in O(log(n)) time,

    Args:
        x ([number]): [the item that acts as the needle]
        s_list ([list[number]]): [list]

    Returns:
        [number]: [index of new element]

    Example:
        2.5, [0, 1, 2, 3, 4] -> 3
        3, [] -> 0
        1, [1,1,1,1,1,1,2] -> 6
    """
    list_len = len(s_list)
    floor = 0
    roof = list_len
    while floor != roof:
        needle_idx = (floor + roof) // 2
        if x < s_list[needle_idx]:
            roof = needle_idx
        elif x >= s_list[needle_idx]:
            floor = needle_idx + 1
    return roof


def binary_insert_sorted(x, s_list):
    """inderts a value in a sorted array. Does not work if the array is not sorted. time complexity O(n)

    Args:
        x ([number]): [description]
        s_list ([type]): [description]

    Example:
        3.5, [1,2,3,4] -> [1,2,3,3.5,4]
        9, [] -> [9]
    """
    s_list.insert(_binary_find(x, s_list), x)
    # print(s_list)


def insertion_sort(s_list):
    """sorts a list using the insertion sort algorthm with a time complexity of O(n^2)

    Args:
        s_list ([list[number]]): [unsorted list]

    Returns:
        [list[number]]: [sorted list]

    Example:
        [] -> []
        [3,2,1] -> [1, 2, 3]
    """
    loop_list = []
    s_len = len(s_list)
    for i in range(s_len):
        binary_insert_sorted(s_list[i], loop_list)
    return loop_list


# //==== uppgift 2 =====\\
def count_words(filename):
    """counts the words, ie characters seperated by a whitespace, in a file

    Args:
        filename ([string]): [a filename parsed as a string]

    Returns:
        [int]: [number of words]

    Example:
        count_words(input.txt) -> 42
    """
    return len(open(filename).read().split())


# //====uppgift 3 ====\\
def annotate(filename):
    """reads each row in a file and creates another file named 'annotate.txt' where it appends word count and line number to each row

    Args:
        filename ([string]): [a filename parsed as a string]

    Example:
        '
        The quick brown fox jumps over a lazy dog 0 9
        Waltz, bad nymph, for quick jigs vex. 1 16
        Pack my box with five dozen liquor jugs. 2 24
        The five boxing wizards jump quickly. 3 30
        '
    """
    f = open(filename)
    words = 0
    a_file = open("annotate.txt", "w")
    for idx, line in enumerate(f):
        words += len(line.split())
        a_file.write(line.replace("\n", "") + " " + str(idx) + " " + str(words) + "\n")


# //==== uppgift 4 ====\\
def save_rows(h):
    """Grabs all lines of text from a file handle, and returns a dict where the keys are the line number, starting at 0

    Args:
        h ([file handle]): [a file handle. check example for example.]

    Returns:
        [dict]: [dictionary where line number are keys and lines are values.]

    Example:
        h = open('loremipsum.txt')
        save_rows(h) ->
        '
        dict: {0: 'The quick brown fox jumps over a lazy dog\n', 1: 'Waltz, bad nymph, for quick jigs vex.\n', 2: 'Pack my box with five dozen liquor jugs.\n', 3: 'The five boxing wizards jump quickly.'}
        '
    """
    mydict = {}
    for idx, line in enumerate(h):
        mydict[idx] = line
    return mydict


def programsnutt():
    """
    Short program that asks for a file name, then asks for row and letter of said file and then prints the char. Does not return anything
    """
    filename = input("Vilken fil vill du läsa in?") or TESTFIL
    # filename = TESTFIL i
    try:
        filhandtag = open(filename)
    except FileNotFoundError:
        print(
            "tyvärr så finns det ingen fil med rätt namn. Kolla så att din terminal befinner sig i rätt mapp, och kom ihåg att skriva rätt file-extension (tex .txt) i slutet"
        )
        return
    mindict = save_rows(filhandtag)
    while True:
        indata = input("skriv in två siffror för rad respektive bokstav i filen som du vill skriva ut, separerat av ett whitespace. Skriv 'exit' när du är klar: \n")
        if indata == "exit":
            return
        x, y = map(int, indata.split())
        if x >= len(mindict) or y >= len(mindict[x]):
            print("Out of bounds")
            return
        print("Space" if mindict[x][y] == " " else mindict[x][y])


def main():
    # uppgift 1
    print("insertion sort:", insertion_sort([random.randrange(0, 100) for _ in range(25)]))
    # uppgift 2
    print("antal ord:", count_words(TESTFIL))
    # upg 3
    annotate(TESTFIL)
    # upg 4
    filhandtag = open(TESTFIL)
    print("dict:", save_rows(filhandtag))
    programsnutt()


if __name__ == "__main__":
    main()

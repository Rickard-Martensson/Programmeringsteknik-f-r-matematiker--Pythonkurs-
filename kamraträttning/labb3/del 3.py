# Laboration 3


# Uppgift 1a:
# Define a function that tests if the elements in a list are sorted


def is_sorted(my_list):

    for i in range(0, len(my_list) - 1):
        if len(my_list) in (0, 1):  # for empty lists and lists with one element
            return True
        elif my_list[i] > my_list[i + 1]:  # for lists with len >= 2, if one element is
            return False  # bigger then the following
    return True


print("Uppgif 1a:")
print(is_sorted([1, 4, 23, 101, 2912]))
print(is_sorted([]))
print(is_sorted([-1]))
print(is_sorted([2, 4, 1]))


# Uppgift 1b:
# Create a function that inserts an element x in a sorted list
def insert_in_sorted(x, my_list):

    if not is_sorted(my_list):
        raise ValueError("Input list must be sorted")  # Error message

    for i in range(len(my_list)):
        if my_list[i] > x:
            my_list.insert(i, x)  # insert x after the i
            return my_list
    my_list.append(x)
    return my_list


print("Uppgift 1b:")
print(insert_in_sorted(2, []))
print(insert_in_sorted(5, [0, 1, 3, 4]))
print(insert_in_sorted(2, [0, 1, 2, 3, 4]))
# print(insert_in_sorted(2, [3,1]))
print(insert_in_sorted(2, [2, 2]))


# Uppgift 1c:
# Create a function that sorts a list, with insert_in_sorted


def insertion_sort(my_list):
    out = []

    for i in my_list:
        insert_in_sorted(i, out)  # Using insert_in_sorted to sort the list "out"
    return out


print("Uppgift 1c")
print(insertion_sort([12, 4, 3, -1]))
print([])


# Uppgift 2:
# Create a function that returns the number of words from a file


def count_words(f):
    list1 = []

    with open(f) as h:
        list1 = h.read()  # Reading the file
        list1 = list1.replace("\n", " ")  # Removing the "\n" signs so they dont count
        return len(list1.split())


print("Uppgift 2:")
print(count_words("input.txt"))


# Uppgift 3:
# Write a function that prints a file, and in the end of the line adds
# row number and number of words up until and with that row included.


def annotate(f):
    words_num = 0
    out = ""

    with open(f, "r") as h, open("annotated.txt", "w") as h_out:
        lines = h.readlines()
        for i, line in enumerate(lines):
            words_num += len(line.split())
            if line[-1] == "\n":  # For the rows that are followed by another row
                out += line.replace("\n", " " + str(i) + " " + str(words_num) + "\n")
                # Replace the \n with row number, number of words and add row change
            else:  # for the last row
                out += line + " " + str(i) + " " + str(words_num)
                # Just add row number and number of words in the end of line
        h_out.write(out)


# Uppgift 4a:
# Create a function that save row number as keys and the lines as values


def save_rows(h):
    make_list = dict()
    row_num = 0
    lines = h.readlines()

    for i, line in enumerate(lines):
        rows = line.strip("\n")
        make_list[row_num] = rows
        row_num += 1
    return make_list


# Uppgift 4b
# Create a function that asks for a file and coordinates and then returns
# the sign of the "place".


file_question = input("Name the file you want to use: ")  # Question about name of file
try:
    with open(file_question, "r") as h:
        a = h

except FileNotFoundError:  # If file could not be found, return error text
    print("File could not be found, you wrote: ", file_question)
else:
    with open(file_question) as text:  # open the file they wanted to use
        save_rows_1 = save_rows(text)
        print('At any point type "exit" to quit. ')
        while True:
            row = input("provide row: ")
            if row == "exit":
                break
            row = int(row)
            column = input("provide column: ")
            if column == "exit":
                break
            column = int(column)
            if len(save_rows_1) <= row or len(save_rows_1[row]) <= column:
                print("Out of bounds")  # If len of row or len of column is to high
            else:
                out = save_rows_1[row][column]
                if out == " ":
                    print("Space")
                else:
                    print(out)

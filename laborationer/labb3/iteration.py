import random  # only used for debugging, not the algorithm itself


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


def count_rows(filename):
    f = open(filename)
    lines = 0
    while f.readline():
        lines += 1
    return lines


def annotate(filename):
    f = open(filename)


print(count_rows("loremipsum.txt"))


def main():
    my_list = [i for i in range(30)]
    binary_insert_sorted(13.5, my_list)
    binary_insert_sorted(3, [])

    # print(_binary_find(1, [1, 1, 1, 1, 1, 1, 2]))

    # print(insertion_sort([random.randrange(0, 100) for _ in range(25)]))


if __name__ == "__main__":
    main()

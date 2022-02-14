# Note: This code is obviously not how you write a library. I've made it easy-to-read rather than actually good.

def read_data(filename):
    """
    Opens a data-file, read the data and add it to a dict.
    The data comes in the form of
        1, 0.1, 0.2, 73
        1, 0.11, 0.1, 101
        2, 0.23, 0.01, 17
        2, 0.12, 0.15, 23
    where every row has the form:
    [int (batch number)], [x-pos (float)], [y-pos (float)], [measurement (int)]

    Adds the data [x-pos, y-pos, measurement] to the dict with key=[batch_number], then returns the dict

    Args:
        filename ([string]): [a string thats the filename, for example 'sample1.txt']

    Returns:
        dict ([dict]): [a dictionary where each key (batch-number) has a value [list of tuples, each typle has a (x-pos, y-pos, measurement) ] ]

    Example usage:
        read_data('sample1.txt') -> data
            sample1.txt:
                1, 0.1, 0.2, 73
                1, 0.11, 0.1, 101
                2, 0.23, 0.01, 17
                2, 0.12, 0.15, 23
            data:
                {1: [(0.1, 0.2, 73), (0.11, 0.1, 101)], 2: [(0.23, 0.01, 17), (0.12, 0.15, 23)]}
    """
    data = dict()  # Or data = {}
    batch_number = 0
    with open(filename, "r") as h:
        try:
            for line in h:
                row = line.split(",")
                batch_number, measurement = int(row[0]), int(row[3])
                x_coordinate, y_coordinate = float(row[1]), float(row[2])
                if not batch_number in data:
                    data[batch_number] = []
                data[batch_number] += [(x_coordinate, y_coordinate, measurement)]
        except ValueError as e:
            print(e, "at batch number", batch_number)
        except Exception as e:
            print("something else went wrong")
            print(e)

    return data


def display_data(data):
    """
    Displays data previously collected.
    Sums all data where the x, y coordinates are within the unit circle. if true, it 
    Displays it in order, ie batch 1 will be displayed before batch 2.

    Args:
        data ([dict]): [a dictionary where each key (batch-number) has a value [list of tuples, each typle has a (x-pos, y-pos, measurement) ] ]

    Example:
        display_data(data) ->
            1        15.0
            2        200.0
            3        1500.0

        data:
            3, 0.5, 0.5, 1000
            1, 0.1, 0.2, 10
            3, 0.5, 0.5, 2000
            1, 0.11, 0.1, 20
            2, 0.23, 0.01, 100
            2, 0.23, 0.01, 200
            2, 0.12, 0.15, 300

    """
    sorted_data = []
    for batch, sample in data.items():
        sorted_data.append((batch, sample))
    sorted_data = sorted(sorted_data, key=lambda x: x[0])
    for batch, sample in sorted_data:
        if len(sample) > 0:
            n = 0
            x_sum = 0
            for datapoint in sample:
                x_pos = datapoint[0]
                y_pos = datapoint[1]
                val = datapoint[2]
                if x_pos ** 2 + y_pos ** 2 <= 1:
                    x_sum += val
                    n += 1
            if n > 0:
                average = x_sum / n
                print(batch, "\t", average)
            else:
                print("no datapoints in batch", batch, "exist withing the unit circle")
        else:
            print(batch, "\tNo data")


if __name__ == "__main__":
    filename = input("Which data file? ") or "sample5.txt"
    my_data = read_data(filename)
    print(read_data(filename))
    display_data(my_data)

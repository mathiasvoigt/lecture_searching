import os

# get current working directory path
cwd_path = os.getcwd()
import json



def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open("sequential.json", "r") as data_file:
        data = json.load(data_file)

    for key in data.keys():
        if field == key:
            sequential_data = data[field]
            return sequential_data
    return None


def linear_search(sequence, number):
    positions = []
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == number:
            positions.append(i)
            count = count + 1
    return {"positions": positions, "count": count}


def pattern_search(sequence, pattern=""):

    positions = set()
    seq_lenght = len(sequence)
    pattern_lenght = len(pattern)

    for i in range(seq_lenght - pattern_lenght + 1):
        if sequence[i:i+pattern_lenght] == pattern:
            positions.add(i)

    return positions


def binary_search(sequence, number):
    left, right = 0, len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2
        if sequence[mid] == number:
            return mid
        elif sequence[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return None



def main():
    sequential_data = read_data("sequential.json", "ordered_numbers")
    index = binary_search(sequential_data, 22)
    print(index)
    return


if __name__ == '__main__':
    main()
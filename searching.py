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
        else:
            return None

    with open(file_path) as data_file:
        data = json.load(data_file)

    return data.get(field, None)

def linear_search(sequence, number):
    positions = []
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == number:
            positions.append(i)
            count = count + 1
    return {"positions": positions, "count": count}


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Sequential_data", sequential_data)
    dictionary = linear_search(sequential_data, 0)
    print(dictionary)
    return


if __name__ == '__main__':
    main()
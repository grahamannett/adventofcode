from typing import List


def split_data(data: str) -> List[str]:
    return data.split("\n")


def read_data(file: str) -> List[str]:
    with open(file, "r") as f:
        data = f.read()

    return split_data(data)


def parse_input(data):
    data_len = len(data)
    idx_counter = [0 for _ in range(len(data[0]))]
    for row in data:

        for idx, val in enumerate(row):
            idx_counter[idx] += int(val)

    return idx_counter, data_len


def count_vals_part_a(data):
    gamma = []
    eps = []

    data_length = len(data)
    idx_counter = [0 for _ in range(len(data[0]))]

    for row in data:
        for idx, val in enumerate(row):

            idx_counter[idx] += int(val)

    for val in idx_counter:
        if val < data_length / 2:
            gamma.append(0)
            eps.append(1)
        else:
            gamma.append(1)
            eps.append(0)

    gamma = "".join([str(val) for val in gamma])
    eps = "".join([str(val) for val in eps])

    gamma = int(gamma, 2)
    eps = int(eps, 2)
    return gamma * eps


test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


if __name__ == "__main__":
    print(count_vals_part_a(split_data(test_input)))
    print(count_vals_part_a(read_data("day3_input")))

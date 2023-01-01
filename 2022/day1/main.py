def read_file(file: str):
    data = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                line = int(line)

            data.append(line)
    return data


def sum_values_between_empty(data: list[int]):
    sums = []
    running_sum = 0
    for line in data:
        if line == "":
            sums.append(running_sum)
            running_sum = 0
        else:
            running_sum += line

    sums = sorted(sums)
    return sums


file1 = read_file("input1")
sums = sum_values_between_empty(file1)
print(sums[-1])

print("---")
print(sums[-3] + sums[-2] + sums[-1])

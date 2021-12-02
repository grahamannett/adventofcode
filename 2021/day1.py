from typing import List

def file_to_array(file: str) -> List[int]:
    with open(file, "r") as f:
        data = f.read()

    data = data.split("\n")

    clean_data = []
    for line in data:
        if line.isnumeric():
            clean_data.append(int(line))

    return clean_data


def count_increments_part_a(arr: List[int]):
    count = 0
    for idx in range(1, len(arr)):

        if arr[idx-1] < arr[idx]:
            count += 1
    return count


def count_increments_part_b(arr: List[int]):
    count = 0

    for idx in range(1, len(arr)+1):
        prev_window = arr[idx - 1:idx +2]
        window = arr[idx:idx+3]
        if sum(window) > sum(prev_window):
            count += 1

    return count




arr2= [
607,
618,
618,
617,
647,
716,
769,
792,
]


print(count_increments_part_a(file_to_array("day1_input")))
print(count_increments_part_b(file_to_array("day1_input")))
print(count_increments_part_b(arr2))

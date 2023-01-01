from typing import Dict, List
from collections import defaultdict


def read_file(file: str) -> List[str]:
    data = []
    with open(file, "r") as f:
        return f.read().splitlines()


def item_count(items: str) -> Dict[str, int]:
    count = defaultdict(int)
    for char in items:
        count[char] += 1
    return count


def char_to_int(char: str) -> int:
    if char.isupper():
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96


def part1(lines: List[str]):
    s = 0
    for line in lines:
        mid = int(len(line) / 2)
        first, second = line[:mid], line[mid:]
        assert (len(first) + len(second)) == len(line)

        first_count, second_count = item_count(first), item_count(second)

        intersect = set(first_count.keys()) & set(second_count.keys())

        char = intersect.pop()
        val = char_to_int(char)
        # print(char, val)
        s += val

    return s


def part2(lines: List[str]) -> int:
    step_size = 3
    s = 0
    for g_idx in range(0, len(lines), step_size):
        items = [item_count(e) for e in lines[g_idx : g_idx + step_size]]
        item_set = [{*i.keys()} for i in items]
        shared_item = item_set[0] & item_set[1] & item_set[2]
        char = shared_item.pop()
        val = char_to_int(char)
        s += val

    return s


example1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

# print(part1(example1))
# print(part1(read_file("input1")))

print(part2(example1))
print(part2(read_file("input1")))

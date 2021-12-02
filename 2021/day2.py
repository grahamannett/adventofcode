from dataclasses import dataclass
from typing import List, Tuple

class Command:
    _cmd = {
        "forward": 0,
        "down": 1,
        "up": -1
    }

    def __init__(self, val) -> None:
        self.cmd = self._cmd[val]
        self.key = val


    def __repr__(self) -> str:
        return self.key


class Direction:
    def __init__(self, *args, **kwargs):
        self.cmd = Command(args[0])
        self.val = int(args[1])

    def __repr__(self) -> str:
        return f"{self.cmd} - {self.val}"

    def depth(self):
        if self.cmd.cmd != 0: return True


def read_data(file: str) -> List[str]:
    with open(file, "r") as f:
        data = f.read()

    data = data.split("\n")
    return data

def arr_to_type(arr: str) -> List[Direction]:
    clean_data = []
    for line in arr:
        line = line.split(" ")
        d = Direction(*line)
        clean_data.append(d)

    return clean_data


class Position:
    horizontal = 0
    depth = 0

    def __repr__(self) -> str:
        return f"horizontal: {self.horizontal} \ndepth: {self.depth}"

def get_position_part_a(data: List[Direction]) -> Position:
    p = Position()

    for direction in data:
        if direction.depth():
            p.depth += direction.cmd.cmd * direction.val
        else:
            p.horizontal += direction.val
        # print(p)
    return p


class PositionAim:
    aim = 0
    horizontal = 0
    depth = 0

    def __repr__(self) -> str:
        return f"horizontal: {self.horizontal} \ndepth: {self.depth}"


def get_position_part_b(data: List[Direction]) -> PositionAim:
    p = PositionAim()

    for direction in data:
        if direction.depth():
            p.aim += direction.val * direction.cmd.cmd
        else:
            p.horizontal += direction.val
            p.depth += (p.aim * direction.val)

    return p

test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""



# print(get_position_part_a(arr_to_type(test_input.split("\n"))))
# print(get_position_part_b(arr_to_type(test_input.split("\n"))))


print(get_position_part_a(arr_to_type(read_data("day2_input"))))

print("---")
print(get_position_part_b(arr_to_type(read_data("day2_input"))))
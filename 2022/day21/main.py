from typing import List, Tuple, NamedTuple
from dataclasses import dataclass

import operator

OpFunc = {
    "+": operator.add,
    "*": operator.mul,
    "-": operator.sub,
    "/": operator.truediv,
}

OpFuncOpposite = {
    "+": operator.sub,
    "*": operator.truediv,
    "-": operator.add,
    "/": operator.mul,
}


class Operator(NamedTuple):
    left: str
    op: str
    right: str


@dataclass
class Monkey:
    name: str
    val: int | Operator = None

    def get(self) -> int:
        if isinstance(self.val, int):
            return self.val

        func = OpFunc[self.val.op]
        try:
            out = func(self._monkeys[self.val.left], self._monkeys[self.val.right].get())
        except:
            breakpoint()
        return out


def read_file(filename: str) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


def part1(lines: List[str]) -> int:
    monkeys = {}

    for line in lines:
        monkey_name, rest = line.split(":")

        rest = rest.lstrip()

        val = int(rest) if rest.isnumeric() else Operator(*rest.split(" "))

        monkey = Monkey(monkey_name, val)
        monkey._monkeys = monkeys
        monkeys[monkey_name] = monkey

    root = monkeys["root"].get()
    breakpoint()
    return root


def part2(lines: List[str]) -> int:
    monkeys = {}
    for line in lines:
        monkey_name, rest = line.split(":")
        rest = rest.lstrip()
        val = int(rest) if rest.isnumeric() else Operator(*rest.split(" "))
        monkey = Monkey(monkey_name, val)
        monkey._monkey = monkeys
        monkeys[monkey_name] = monkey

    return monkeys["root"]


print(part1(read_file("input1")))
# out = part2(read_file("input1"))
breakpoint()

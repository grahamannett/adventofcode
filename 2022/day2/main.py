from dataclasses import dataclass
from typing import List

MovePoints = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

OutcomePoints = {
    "lose": 0,
    "draw": 3,
    "win": 6,
}

MoveToString = {
    # them
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    # me
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

OutcomeFromChar = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


@dataclass
class Move:
    opp: str
    my: str

    def part_1(self):
        self.opp = MoveToString[self.opp]
        self.my = MoveToString[self.my]

    def part_2(self):
        self.opp = MoveToString[self.opp]
        o = self.opp

        s = OutcomeFromChar[self.my]

        if (s == "lose" and o == "rock") or (s == "win" and o == "paper") or (s == "draw" and o == "scissors"):
            my_move = "scissors"
        elif (s == "lose" and o == "scissors") or (s == "win" and o == "rock") or (s == "draw" and o == "paper"):
            my_move = "paper"
        elif (s == "lose" and o == "paper") or (s == "win" and o == "scissors") or (s == "draw" and o == "rock"):
            my_move = "rock"
        else:
            breakpoint()

        outcome_points = OutcomePoints[s]
        move_point = MovePoints[my_move]
        return outcome_points + move_point

    def calc_my_point(self):
        return MovePoints[self.my]

    def round_outcome(self):
        if self.opp == "rock" and self.my == "paper":
            return 6
        elif self.opp == "paper" and self.my == "scissors":
            return 6
        elif self.opp == "scissors" and self.my == "rock":
            return 6
        elif self.opp == self.my:
            return 3
        else:
            return 0

    def calc_points_part1(self):
        return self.calc_my_point() + self.round_outcome()

    @classmethod
    def from_string(cls, s: str):
        return cls(*s.split(" "))


def read_input(file: str):
    data = []
    with open(file, "r") as f:
        return f.read().splitlines()


# def guide_to_actions(List[str]):
def part1(move_list: List[str]) -> int:
    moves = []
    points = 0
    for s in move_list:
        m = Move.from_string(s)
        m.part_1()
        moves.append(m)
        points += m.calc_points_part1()
    return points


def part2(move_list: List[str]) -> int:
    points = 0
    for s in move_list:
        m = Move.from_string(s)
        points += m.part_2()
    return points


input1 = read_input("input1")
example1 = """A Y
B X
C Z""".splitlines()

# print(part1(example1))
# print(part1(input1))

# print(part2(example1))
print(part2(input1))

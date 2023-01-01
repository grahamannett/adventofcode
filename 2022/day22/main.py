from typing import List, Tuple
from dataclasses import dataclass


def read_file(filename: str) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


@dataclass
class Move:
    direction: str
    distance: int


class Direction:
    _directions = [
        # [up/down, left/right]
        [0, 1],  # right
        [1, 0],  # down
        [0, -1],  # left
        [-1, 0],  # up
    ]

    def __init__(self):
        self._dir_val = 0
        # self.direction = direction

    @property
    def direction(self):
        return self._directions[self._dir_val]

    def next(self, direction: str):
        if direction == "R":
            self._dir_val = (self._dir_val + 1) % 4
        elif direction == "L":
            self._dir_val = (self._dir_val - 1) % 4
        else:
            raise ValueError("Invalid direction")


MAP_VALUES = {
    " ": -1,  # empty
    ".": 0,  # clean
    "#": 1,  # wall
}

MAP_VALUES_INV = {v: k for k, v in MAP_VALUES.items()}


def make_map(raw_map: List[str]) -> List[List[int]]:
    longest_row = max(raw_map, key=len)
    map_ = []
    for raw_row in raw_map:
        row = []
        for val in raw_row:
            if val in MAP_VALUES:
                row.append(MAP_VALUES[val])
            else:
                breakpoint()
                raise ValueError("Invalid map value")

        if len(row) < len(longest_row):
            row += [-1] * (len(longest_row) - len(row))
        map_.append(row)

    return map_


# class Map:
#     def __init__(self, raw_map: List[str]):
#         self.raw_map = raw_map
#         self.width = len(raw_map[0])
#         self.height = len(raw_map)

#         self._map = self.make_map()

#     def make_map(self):
#         for raw_row in self.raw_map:
#             row = []
#             for val in raw_row:
#                 if val == " ":
#                     row.append(None)
#                 elif val == ".":
#                     row.append(0)
#                 elif val == "#":
#                     row.append(1)
#                 else:
#                     raise ValueError("Invalid map value")


class Player:
    def __init__(self, map: List[List[int]]):
        self.map = map
        self.map_height = len(map)
        self.map_width = len(map[0])

        self.position = self.start_position()
        self.direction = Direction()

    def start_position(self):
        for i, val in enumerate(self.map[0]):
            if val is not -1:
                return [0, i]

    def fix_bounds(self, next_position: Tuple[int, int]):
        if next_position[0] < 0:
            next_position[0] = self.map_height - 1
        if next_position[0] >= self.map_height:
            next_position[0] = 0
        if next_position[1] < 0:
            next_position[1] = self.map_width - 1
        if next_position[1] >= self.map_width:
            next_position[1] = 0
        return next_position

    def _move(self):
        direction = self.direction.direction
        next_position = direction[0] + self.position[0], direction[1] + self.position[1]

        # def check_next_move(self):

        #     move_allowed = True
        #     direction = self.direction.direction

        #     while True:
        #         next_position = [direction[0] + self.position[0], direction[1] + self.position[1]]
        #         next_position = self.fix_bounds(next_position)
        #         next_map_position = self.map[next_position[0]][next_position[1]]
        #         if next_map_position == 1:
        #             break
        #         elif ne
        #         breakpoint()
        #         break
        #         # if next_position in MAP_VALUES_INV:

        #     # map_position = self.map[next_position[0]][next_position[1]]
        #     # if map_position is None:

        return move_allowed

    def turn(self, direction: str):
        self.direction.next(direction)

    def check_map(self, position: Tuple[int, int]):
        map_position = self.map[position[0]][position[1]]
        if map_position is -1:
            return False
        return True

    def check_next_move(self, position: Tuple[int, int], direction: Tuple[int, int]):
        next_position = [direction[0] + position[0], direction[1] + position[1]]
        next_position = self.fix_bounds(next_position)
        map_position = self.map[next_position[0]][next_position[1]]
        if next_position == -1:
            return self.check_next_move(next_position, direction)
        elif next_position == 0:
            return True
        elif next_position == 1:
            return False

    def move(self, move: Move):

        self.turn(move.direction)
        amt_to_move = move.distance

        position = self.position
        direction = self.direction.direction

        while amt_to_move > 0:
            move_allowed = self.check_next_move(position, direction)
            if move_allowed == False:
                break
            amt_to_move -= 1


def parse_moves(raw_directions: str) -> List[Move]:
    moves = []
    val: str = ""

    magnitude = []
    for i, val in enumerate(raw_directions):
        if val.isalpha():
            moves.append(Move(val, int("".join(magnitude))))
            magnitude = []
        else:
            magnitude.append(val)

    return moves


def part1(data: List[str]) -> int:
    raw_map, raw_directions = data[:-2], data[-1]

    moves = parse_moves(raw_directions)
    map_ = make_map(raw_map)

    player = Player(map=map_)
    # breakpoint()

    # breakpoint()

    for move in moves:
        player.move(move)
    breakpoint()


data = read_file("input1")
part1(data)
breakpoint()

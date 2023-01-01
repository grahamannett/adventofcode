from dataclasses import dataclass
from typing import Any, Sequence, List


@dataclass
class Cube:
    x: int
    y: int
    z: int

    # to_x_1: Cube
    # to_x_: Cube


def _make_dim(dim: Sequence[int]):
    if len(dim) == 1:
        return [0 for _ in range(dim[0])]
    else:
        return [_make_dim(dim[1:]) for _ in range(dim[0])]


class Tensor:
    list
    def __init__(self, shape: Sequence[int]):
        self.data = _make_dim(shape)

    def __getitem__(self, idx: int | tuple):
        if isinstance(idx, int):
            return self.data[idx]
        elif isinstance(idx, tuple):
            rest = idx[1:]
            return self.data[idx[0]
        # for dim in shape:


def read_file(file: str):
    data = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                line = int(line)

            data.append(line)
    return data


def coords_to_3d(file: list[int]):
    pass


t = Tensor([3, 2, 4])

t[1, 1:, 1]

# from typing import Sequence


# def _make_dim(dim: Sequence[int]):
#     if len(dim) == 1:
#         return [0 for _ in range(dim[0])]
#     else:
#         return [_make_dim(dim[1:]) for _ in range(dim[0])]


# data = _make_dim([3, 3, 3])
# breakpoint()

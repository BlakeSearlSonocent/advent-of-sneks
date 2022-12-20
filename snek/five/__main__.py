import re
from itertools import groupby

from numpy import sign

from snek.file_utils import file_to_string_list

if __name__ == "__main__":
    line_ends = [
        ((int(x_1), int(y_1)), (int(x_2), int(y_2)))
        for line in file_to_string_list("five/input.txt")
        for x_1, y_1, x_2, y_2 in re.findall("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", line)
    ]

    points = []
    for start, end in line_ends:
        start_x, start_y = start
        end_x, end_y = end
        dx = end_x - start_x
        dy = end_y - start_y

        moves = max(abs(dx), abs(dy))
        move_x, move_y = sign(dx), sign(dy)
        positions = [(start_x + (i * move_x), start_y + (i * move_y)) for i in range(moves + 1)]
        points.extend(positions)

    print(len([key for key, group in groupby(sorted(points)) if len(list(group)) > 1]))

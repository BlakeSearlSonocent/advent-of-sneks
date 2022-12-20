from numpy import median

from snek.file_utils import read_input


def part_one():
    locations = list(map(int, read_input("seven/input.txt").split(",")))
    mid = int(median(locations))
    print(sum(abs(x - mid) for x in locations))


def part_two():
    locations = list(map(int, read_input("seven/input.txt").split(",")))
    print(
        min(
            sum((abs(x - mid) * (abs(x - mid) + 1) // 2) for x in locations)
            for mid in range(min(locations), max(locations) + 1)
        )
    )


if __name__ == "__main__":
    part_one()
    part_two()

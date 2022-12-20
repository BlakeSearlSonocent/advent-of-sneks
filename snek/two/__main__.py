from snek.file_utils import file_to_string_pairs


if __name__ == "__main__":
    commands = [(cmd, int(magnitude)) for cmd, magnitude in file_to_string_pairs("two/input.txt")]

    x, y, aim = 0, 0, 0
    for direction, magnitude in commands:
        if direction == "up":
            aim -= magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "forward":
            x += magnitude
            y += aim * magnitude

    print(x * y)

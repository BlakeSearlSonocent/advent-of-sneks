from utils import *

commands = read_lines("2")

x, y, aim = 0, 0, 0
for command in read_lines("2"):
    direction, magnitude_string = command.split()
    magnitude = int(magnitude_string)

    if direction == "up":
        aim -= magnitude
    elif direction == "down":
        aim += magnitude
    elif direction == "forward":
        x += magnitude
        y += (aim * magnitude)

print(x * y)

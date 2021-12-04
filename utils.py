def read_ints(filename):
    with open("../inputs/" + filename + ".txt") as f:
        for line in f:
            yield int(line)


def read_lines(filename):
    with open("../inputs/" + filename + ".txt") as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

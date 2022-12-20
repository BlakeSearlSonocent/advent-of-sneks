from snek.file_utils import file_to_string_list


def part_one():
    binaries = file_to_string_list("three/input.txt")

    gamma = ""
    for i in range(len(binaries[0])):
        col_bits = [binaries[j][i] for j in range(len(binaries))]
        gamma += "1" if col_bits.count("1") > col_bits.count("0") else "0"

    epsilon = "".join(map(str, [1 - int(x) for x in gamma]))
    print(int(gamma, 2) * int(epsilon, 2))


def part_two():
    binaries = file_to_string_list("three/input.txt")
    oxygen = binaries

    i = 0
    while len(oxygen) > 1:
        col_bits = [oxygen[j][i] for j in range(len(oxygen))]
        most_common = "1" if col_bits.count("1") >= col_bits.count("0") else "0"
        oxygen = [binary for binary in oxygen if binary[i] == most_common]
        i += 1

    carbon = binaries
    i = 0
    while len(carbon) > 1:
        col_bits = [carbon[j][i] for j in range(len(carbon))]
        most_common = "0" if col_bits.count("0") <= col_bits.count("1") else "1"
        carbon = [binary for binary in carbon if binary[i] == most_common]
        i += 1

    print(int(oxygen[0], 2) * int(carbon[0], 2))


if __name__ == "__main__":
    part_one()
    part_two()

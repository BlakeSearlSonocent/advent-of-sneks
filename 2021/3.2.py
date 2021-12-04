from utils import *

binaries = read_lines("3")
oxygen = binaries

i = 0
while len(oxygen) > 1:
    colBits = [oxygen[j][i] for j in range(len(oxygen))]
    mostCommon = '1' if colBits.count('1') >= colBits.count('0') else '0'
    oxygen = [binary for binary in oxygen if binary[i] == mostCommon]
    i += 1

carbon = binaries
i = 0
while len(carbon) > 1:
    colBits = [carbon[j][i] for j in range(len(carbon))]
    mostCommon = '0' if colBits.count('0') <= colBits.count('1') else '1'
    carbon = [binary for binary in carbon if binary[i] == mostCommon]
    i += 1

print(int(oxygen[0], 2) * int(carbon[0], 2))

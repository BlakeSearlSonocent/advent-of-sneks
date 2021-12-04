from utils import *

binaries = read_lines("3")

gamma = ''
for i in range(len(binaries[0])):
    colBits = [binaries[j][i] for j in range(len(binaries))]
    gamma += '1' if colBits.count('1') > colBits.count('0') else '0'

epsilon = ''.join(map(str, [1 - int(x) for x in gamma]))
print(int(gamma, 2) * int(epsilon, 2))
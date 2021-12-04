from utils import *
from

d = list(read_ints("1"))
print([sum(x < y for x, y in zip(d, d[w:])) for w in [1, 3]])

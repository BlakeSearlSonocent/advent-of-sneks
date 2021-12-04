from utils import *

depths = list(read_ints("1"))
decreases = sum(x[0] < x[1] for x in list(zip(depths, depths[1:])))
print(decreases)
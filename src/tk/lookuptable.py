import math
cache = {}


def build_lookup_table():
    for i in range(1, 1000):
        inv_square_root(i)


def inv_square_root(n):
    if n not in cache:
        cache[n] = 1 / math.sqrt(n)
    return cache[n]


for i in range(1, 6):
    print(inv_square_root(i))

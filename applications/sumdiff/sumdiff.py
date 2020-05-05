from itertools import product
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)

For the above q, we get this sample output:

f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
f(1) + f(4) = f(12) - f(4)    10 + 22 = 54 - 22
f(4) + f(1) = f(12) - f(4)    22 + 10 = 54 - 22
f(1) + f(7) = f(12) - f(1)    10 + 34 = 54 - 10
f(4) + f(4) = f(12) - f(1)    22 + 22 = 54 - 10
f(7) + f(1) = f(12) - f(1)    34 + 10 = 54 - 10
f(3) + f(3) = f(12) - f(3)    18 + 18 = 54 - 18
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# First, get all possible combinations of groups of 4 of q
# combos = combinations_with_replacement(list(q), 4)
combos = product(q, repeat=4)

# Initialize a dict to store results of calling f()
result_dict = dict()

for line in combos:
    # print(line)
    # Calculate left side and right side and see if they are equal

    first = 0
    second = 0
    third = 0
    fourth = 0

    # For each call of f(), check first to see if result is in the dictionary
    if result_dict.get(line[0]):
        first = result_dict[line[0]]
    else:
        first = f(line[0])
        result_dict[line[0]] = first

    if result_dict.get(line[1]):
        second = result_dict[line[1]]
    else:
        second = f(line[1])
        result_dict[line[1]] = second

    if result_dict.get(line[2]):
        third = result_dict[line[2]]
    else:
        third = f(line[2])
        result_dict[line[2]] = third

    if result_dict.get(line[3]):
        fourth = result_dict[line[3]]
    else:
        fourth = f(line[3])
        result_dict[line[3]] = fourth

    left_side = first + second
    right_side = third - fourth
    # print(f"{left_side} vs {right_side}")
    if left_side == right_side:
        # f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
        # print('found one')
        print(
            f"f({line[0]}) + f({line[1]}) = f({line[2]}) - f({line[3]})  {f(line[0])} + {f(line[1])} = {f(line[2])} - {f(line[3])}")

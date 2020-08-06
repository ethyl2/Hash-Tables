from itertools import product
import time
"""
This version will try populating a dict right at the beginning with all the values for f() using possible inputs.

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

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)
# q = set(range(1, 50))
# q = set(range(1, 25))


def f(x):
    return x * 4 + 6


# First, get all possible combinations of groups of 4 of q
# combos = combinations_with_replacement(list(q), 4)
start_time = time.time()
combos = product(q, repeat=4)

# Initialize dicts to store results of calling f(), doing the left sum, and finding the right difference
result_dict = dict()

for i in range(1, len(q) + 1):
    result_dict[i] = f(i)
'''
# These were not making the code run any faster, so I commented them out for now.
sum_dict = dict()
diff_dict = dict()
'''
# print(len(result_dict.keys()))

for line in combos:
    # Calculate left side and right side and see if they are equal
    first = result_dict[line[0]]
    second = result_dict[line[1]]
    third = result_dict[line[2]]
    fourth = result_dict[line[3]]
    '''
    # Check to see if sum was already calculated before doing the sum for the left side
    if sum_dict.get(f'{first},{second}'):
        left = sum_dict[f'{first},{second}']
    elif sum_dict.get(f'{second},{first}'):
        left = sum_dict[f'{second},{first}']
    else:
        left = first + second
        sum_dict[f'{first},{second}'] = left
    
    # Check to see if the difference was already calculated before calculating the difference on the right side.
    if diff_dict.get(f'{third},{fourth}'):
        right = diff_dict[f'{third},{fourth}']
    else:
        right = third - fourth
        diff_dict[f'{third},{fourth}'] = right
    '''
    left = first + second
    right = third - fourth

    if left == right:
        print(f"f({line[0]}) + f({line[1]}) = f({line[2]}) - f({line[3]})  {result_dict[line[0]]} + {result_dict[line[1]]} = {result_dict[line[2]]} - {result_dict[line[3]]}")


end_time = time.time()
print(end_time - start_time)

'''
Add up and print the sum of the all of the minimum elements of each inner array:
```
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
```
The expected output is given by:
```
4 + -1 + 9 + -56 + 201 + 18 = 175
```
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code.
Run through the UPER problem solving framework while going through your thought process.

'''


def sum_inners(arr):
    total = 0
# Declare my accumulator.

# Loop through outer array
    for inner_arr in arr:
        # Call min on each inner array
        winner = min(inner_arr)
# Add the result of min() to my accumulator
        total += winner

# Return the accumlator
    return total


print(sum_inners([[8, 4], [90, -1, 3], [9, 62],
                  [-7, -1, -56, -6], [201], [76, 18]]))


'''
Add up and print the sum of the all of the minimum elements of each inner array.
Each array may contain additional arrays nested arbitrarily deep,
in which case the minimum value for the nested array should be added to the total.
```
[
  [8, [4]],
  [[90, 91], -1, 3],
  [9, 62],
  [[-7, -1, [-56, [-6]]]],
  [201],
  [[76, 0], 18],
]
```
The expected output for the above input is:
```
8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
```
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
'''

# Given a array, which may or may not have nested arrays.
# Declare the accumulator AKA total.
# Loop through the array.
# If an element in the array is a number, add it to a list of numbers.
# If an element is an array, use recursion to call the function on that element.
# Add the min of the list of numbers to the total.
# Return the total.


def sum_min(arr):
    # Declare accumulator
    total = 0

    # Helper function
    def sum_min_nested(arr):
        nonlocal total

        # Declare list that will hold non-array elements
        nums = []

        # Loop through the array
        for elem in arr:
            # Check to see if element is a number or a list
            if not isinstance(elem, list):
                # If it is a number, append it to the non-array elements list
                nums.append(elem)
            else:
                # If it is a list, call the function on that element (AKA that sublist)
                sum_min_nested(elem)

        # If there are elements in the non-array elements list, find the min element and add it to total
        if len(nums) > 0:
            total += min(nums)
        return total

    # Call the inner (helper) function
    sum_min_nested(arr)
    return total


# print(sum_min([1, [1, 2]]))

print(sum_min([
    [8, [4]],
    [[90, 91], -1, 3],
    [9, 62],
    [[-7, -1, [-56, [-6]]]],
    [201],
    [[76, 0], 18],
]))

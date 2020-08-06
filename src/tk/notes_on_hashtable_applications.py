from collections import defaultdict
"""
Hash Table Applications
=======================
Speed of search
---------------
Linear search through an array
Network caching
Memoization--expensive calculation
Indexing
--------
Alice: 30
Bob:   40
Charlie: 20
Dave: 20
Beej: 20
"Show me all the people who are age 30."
What do I want to look up by?  <-- that's the key
30: [Alice]
40: [Bob]
20: [Charlie, Dave, Beej]
Given a list of records, need to convert into a hashtable first O(n)
THEN we can do quick lookups
"""
age_dict = {"Alice": 30, "Bob": 40, "Charlie": 20, "Dave": 20, "Beej": 20}
age_hashtable = defaultdict(list)
for item in age_dict.items():
    age_hashtable[item[1]].append(item[0])

print(age_hashtable)
print(age_hashtable[30])
print(age_hashtable[40])
print(age_hashtable[20])
print('\n')


"""
Removing Duplicates
-------------------
"""
data = ['Snail', 'Dolphin', 'Snail']
h = {}
for i in data:
    # Have we seen this data before?
    if i in h:     # same as checking for existence in the set
        continue
    # We've seen it now:
    h[i] = True  # same as adding to a set
    # print(i)

for entry in h:
    print(f'{entry}: {h[entry]}')
print('\n')

print(h)
print('\n')

for entry in h:
    print(entry)
print('\n')

'''
for i in data: O(n)
    for j in data: O(n)
        replace with hash table O(1)
'''

"""
Counting Elements
-----------------
1
5
5
7
9
2
3
9
5
"""
data2 = ['Snail', 'Horse', 'Snail', 'Dolphin', 'Cow', 'Snail']
data3 = [1, 5, 5, 7, 9, 2, 3, 9, 5]
h = {}
for i in data2:
    if i not in h:
        h[i] = 1
    else:
        h[i] += 1

for entry in h:
    print(f'{entry}: {h[entry]}')

h3 = {}
for i in data3:
    if i not in h3:
        h3[i] = 1
    else:
        h3[i] += 1

for entry in h3:
    print(f'{entry}: {h3[entry]}')
"""
Aside
-----
The key in a dict can be any immutable type, including tuples.
h = {
    (1,2): "value1",
    (3,4,5): "value2"
}
"""

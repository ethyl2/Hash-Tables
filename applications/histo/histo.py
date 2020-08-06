import os
import sys
import re
'''
Print a histogram showing the word count for each word, one hash mark for every occurrence of the word.

Output will be first ordered by the number of words, then by the word (alphabetically).

The hash marks should be left justified two spaces after the longest word.

Case should be ignored, and all output forced to lowercase.

Split the strings into words on any whitespace.

Ignore each of the following characters:

" : ; , . - + = / \ | [ ] { } ( ) * ^ &
If the input contains no ignored characters, print nothing.

Sample output (truncated):

the              ################################################
and              ####################################
of               ###################################
a                ########################
'''

# First, import the file

with open(os.path.join(sys.path[0], 'robin.txt'), 'r') as f:
    words = f.read()

# words = 'Cats and dogs and birds and fish dogs birds'
# Split words into individual words
items = words.split()

# Initialize the dict
words_dict = dict()

# Next, format the words
for word in items:
    parsed_word = re.sub(
        r"[\"\&\.\:\;\,\-\+\=\/\\\[\]\{\}\(\)\*\^\&\|\s]", '', word.lower())
    # print(parsed_word)

    if words_dict.get(parsed_word):
        words_dict[parsed_word] += 1
    else:
        words_dict[parsed_word] = 1

# print(words_dict)

# Convert the words_dict into a list, so it can be sorted
words_list = list(words_dict.items())
# print(words_list)

# Sort the list with the highest occurences first, secondarily sorted alphabetically
words_list.sort(key=lambda x: (-x[1], x[0]))
# print(words_list)

# Find the length of the longest word for layout purposes

'''
# Longer way to figure it out
longest_length = len(words_list[0][0])
for entry in words_list:
    if len(entry[0]) > longest_length:
        longest_length = len(entry[0])
# print(longest_length)
'''
# More concise way to figure it out
longest = max([len(x[0]) for x in words_list])
# print(longest)

# Loop through the list to print each entry with specified format
for entry in words_list:
    print(f"{entry[0]}{' ' * (longest - len(entry[0]))}  {'#' * entry[1]}")

import sys
import os
import random

# Read in all the words in one go
'''
1. Read the file input.txt and split it into words.

Don't worry about changing punctuation or capitalization.
For example, a "word" might be "Hello,. Just leave it all in there.
'''
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
    words = f.read()

# words = 'Cats and dogs and birds and fish dogs birds'
items = words.split(' ')

'''
2. Analyze the text, building up the dataset of which words can follow particular words.

(Hint: leave duplicates in for this part. If a the word and is seen following the word
goats multiple times, include all those ands. It'll give more convincing results
because it is modelling the frequency of how often a word follows another word.)

For example, the paragraph:

Cats and dogs and birds and fish dogs birds

could be represented:

Word     Can be followed by
-------- ------------------
Cats     and
and      dogs birds fish
dogs     and birds
birds    and
fish     dogs
'''
# Analyze which words can follow other words

# Initialize words_dict
words_dict = dict()

# Loop through words (items)
for i in range(0, len(items) - 1):
    # get the word
    word = items[i]

    # get the next word
    next_word = items[i + 1]

    # See if the word is already in the dict
    if words_dict.get(word):
        # If so, append the next_word to the list at that word
        words_dict[word].append(next_word)
    else:
        # If not, create a list there and append the next_word to it
        words_dict[word] = []
        words_dict[word].append(next_word)

# print(words_dict)

'''
3. Choose a random "start word" to begin.
Start words are words that begin with a capital, or a " followed by a capital.
'''
# Loop through the dictionary to find the words that start with a capital (or " followed by a capital).
start_words = [word for word in words_dict.keys() if word.istitle()]
# print(start_words)


# TODO: construct 5 random sentences

'''
Loop through:

Print the word.
If it's a "stop word", stop.
Stop words are words that end in any of the punctuation .?!, or that punctuation followed by a ".
Else randomly choose a word that can follow this one.

Stretch Goal:
Make sure there is always a close quote for an opening quote in the sentence.
'''
suff_list_no_quotes = ['.', '?', '!']
suff_list_quotes = ['."', '?"', '!"']
for i in range(5):
    print(f'{i + 1}.')
    start_word = random.choice(start_words)
    if start_word.startswith('"'):
        suff_list = suff_list_quotes
    else:
        suff_list = suff_list_no_quotes
    word = start_word
    print(word)
    while not word.endswith(tuple(suff_list)):
        word = random.choice(words_dict[word])
        print(word, end=" ")
    print('\n')

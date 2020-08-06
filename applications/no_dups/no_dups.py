'''
Input: a string of words separated by spaces. Only the letters a-z are utilized.

Output: the string in the same order, but with subsequent duplicate words removed.

There must be no extra spaces at the end of your returned string.

The solution must be O(n).

# Initialize a dict
# Create a list from string.split(' ')
# Initialize return string with the first word -- NOT adding a space before it
# Interate through the rest of string.split(' ')
# If word is already in dict, continue
# If word is not already in dict, append to return string ' ' + word -- notice the space
# Then add word to dict
# At end, return return string
'''


def no_dups(s):
    if len(s) < 1:
        return ''
    # Initialize dict
    word_dict = dict()

    # Create word list from s
    word_list = s.split(' ')

    # Initialize the return_string with the first word
    return_string = word_list[0]

    # Put the first word in the dict
    word_dict[return_string] = True

    # Loop through the rest of the words
    for word in s.split(' ')[1:]:
        if word_dict.get(word):
            # Don't put the word in the return_string if it's already been put there
            continue
        else:
            # Append the word to the return_string and put the word in the dict
            return_string += ' ' + word
            word_dict[word] = True
    return return_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))

import re
'''
Input
This function takes a single string as an argument.

Hello, my cat. And my cat doesn't say "hello" back.

Output
It returns a dictionary of words and their counts:

{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
Case should be ignored. Output keys must be lowercase.

Key order in the dictionary doesn't matter.

Split the strings into words on any whitespace.

Ignore each of the following characters:

" : ; , . - + = / \ | [ ] { } ( ) * ^ &
If the input contains no ignored characters, return an empty dictionary.

The split() method splits a string into a list.

You can specify the separator; default separator is any whitespace.
'''


def word_count(s):
    # Declare the word_dict
    word_dict = dict()
    # Split the string up into words
    words = s.split()
    if words == ['']:
        return {}
    for word in words:
        parsed_word = re.sub(
            r"[\"\&\.\:\;\,\-\+\=\/\\\[\]\{\}\(\)\*\^\&\|\s]", '', word.lower())

        if parsed_word == '':
            # Ignore the empty string
            continue

        else:

            if word_dict.get(parsed_word):
                # Increment its counter if the word is in the dict
                word_dict[parsed_word] += 1
            else:
                # Initialize the key:value
                word_dict[parsed_word] = 1
    return word_dict


# Original string: 'Hello, my cat. And my cat doesn\'t say "hello" back.'


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("[Hello]{}"))
    print(word_count('Hello, my+= cat. \And: my; cat- &doesn\'t say "hello" /back.'))
    print(word_count(
        '*Th*is is a test of the emergency broadcast ^network. This is only a (test).'))

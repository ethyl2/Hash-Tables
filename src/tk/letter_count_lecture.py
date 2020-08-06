def letter_count(s):
    d = {}
    for c in s:

        if c.isspace():
            continue
        c = c.lower()
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def print_sorted_letter_count(s):
    c = letter_count(s)
    items = list(c.items())
    items.sort(key=lambda e: e[1], reverse=True)
    for i in items:
        print(f'{i[0]}: {i[1]}')


print_sorted_letter_count("aaabbc")
# print_sorted_letter_count("Hello!")
print_sorted_letter_count("The quick brown fox jumps over the lazy dogs")

records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]


def build_index(rec):
    idx = {}
    for r in rec:
        name, dept = r
        if dept not in idx:
            idx[dept] = []
        idx[dept].append(name)
    return idx


idx = build_index(records)
# print all the departments
for i in idx:
    print(i)
# print everyone in Engineering:
print(idx["Engineering"])

# print entire idx
for i in idx:
    print(f'{i}:{idx[i]}')

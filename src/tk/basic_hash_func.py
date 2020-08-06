def basic_hash_func(str, list_size):
    bytes_rep = str.encode()
    print(bytes_rep)

    rep_sum = 0
    for byte in bytes_rep:
        rep_sum += byte

    print(rep_sum)
    return rep_sum % list_size


print(basic_hash_func('hello', 7))
print(basic_hash_func('world', 7))

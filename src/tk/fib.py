# Slow calculation caching
cache = {}


def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


'''
for i in range(10000):
    print(fib(i))
'''


def fib2(n, cache2={}):
    if n <= 1:
        return n

    if n not in cache2:
        cache2[n] = fib2(n-1, cache2) + fib2(n-2, cache2)
    return cache2[n]


for i in range(10000):
    print(fib2(i))

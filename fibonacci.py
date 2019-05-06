"""implement fibonacci series while generator"""


def fibonacci():
    a,b = 1,1
    while True:
        yield a
        a,b = b, a+b

import itertools

print(list(itertools.islice(fibonacci(), 10)))


fib  = fibonacci()

for i in range(10):
    print(next(fib))

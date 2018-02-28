import sys

from math import *
n = 6
if n % 2 == 0:
    max_step = n // 2
else:
    max_step = (n - 1) // 2

cost = 1

def probability(n, m=None, p=None, p2=None):
    if m == 0:
        return 0
    if not p:
        p = 1.0
    if not m:
        m = sum(range(1, n + 1)) / n - cost

    v1 = sum(range(ceil(m), n)) / (n - floor(m) + 1)
    p1 = (n - floor(m) + 1) / n
    v2 = sum(range(1, floor(m))) / floor(m)
    val =  p * ((p1 * v1) + (1 - p1) * v2)

    print(n, m, p, val, sep='\t')

    return val / 1.0 + probability(n, m - 1, 1 - p1)

print(probability(5))

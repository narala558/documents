from math import ceil, floor


def probability(n, m=None, p=None):
    if not m:
        m = sum(range(1, n + 1)) / n - 1
    if floor(float(m)) == 0:
        return 0
    if not p:
        p = 1.0

    if n % 2 == 0:
        v1 = sum(range(ceil(m), n)) / (n - floor(m))
        p1 = (n - floor(m)) / n
    else:
        v1 = sum(range(ceil(m), n)) / (n - floor(m) + 1)
        p1 = (n - floor(m) + 1) / n

    v2 = sum(range(1, floor(m))) / floor(m)
    val = p*((p1*v1) + (1 - p1)*v2)

    print(n, m, p, val, sep='\t')

    return val / 1.0 + probability(n, m - 1, 1 - p1)


print(probability(5))
# print(probability(6))

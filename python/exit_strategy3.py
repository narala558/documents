from math import ceil, floor

n = 50

max_rounds = n // 2
avg = n * (n + 1) / (2 * n)
print(avg)


def foo(m, avg, x):
    if m <= 0:
        return 0

    s1 = [i for i in range(1, n + 1) if i < avg]
    s2 = [i for i in range(1, n + 1) if i > avg]

    p2 = len(s2) / n
    v2 = sum(s2) / len(s2) + x

    p1 = len(s1) / n

    print(m)
    print(s1, avg, s2, x)
    print('p1', p1, 'p2', p2, 'v2', v2)
    print(p2 * v2, p2 * v2 + x)
    print('================================================')
    return p2 * v2 + (p1 * (foo(m - 1, avg - 1, x - 1)))


print(foo(max_rounds, avg - 1, x=0))

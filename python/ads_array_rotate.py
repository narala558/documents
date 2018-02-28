from collections import deque


def array_left_rotation(a, n, k):
    d = deque(a)
    d.rotate(k)
    return list(d)


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
print(n, k, a)
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')

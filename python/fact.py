def foo(n):
    if n <= 0:
        return 1
    print(n)
    print('=====')
    return n * foo(n - 1)


print(foo(3))

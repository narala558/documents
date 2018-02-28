import sys

n = 4

choices = list(range(1, n + 1))
print(choices)


def update_choices(choices, na):
    return [i if i > na else na for i in choices]


def foo(choices, x):
    if choices[1] == choices[-1]:
        print(choices)
        sys.exit()
    avg = round(sum(choices) / n, 2)
    choices = update_choices(choices, avg)
    print(avg, choices)

    return foo(choices, x - 1)


print(foo(choices, x=0))

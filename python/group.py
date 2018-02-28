import functools

from celery import Celery, group

from .t import *


chains = [
    functools.reduce(foo, tasks, sub.s(i, i)) for i in range(2)
]

print(chains)


g = group(*chains)
print(g)

res = g.apply_async(args=[1111])

c = group(
    chain(
        add.s(4), mult.s(2)
    ),
    sub.s(1)
)(3)

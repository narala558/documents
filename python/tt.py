from celery_group_exp import *

tasks = [add, add, add]


chains = [
    functools.reduce(foo, tasks, sub.s(i, i)) for i in range(2)
]

print(chains)


g = group(*chains)
print(g)

res = g.apply_async(args=[1111])


add.delay(0, 4)

print('done')

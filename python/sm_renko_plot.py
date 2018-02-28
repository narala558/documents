import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle


brick_size = 2



def plot_renko(bricks, brick_size):
    fig = plt.figure(1)
    fig.clf()
    axes = fig.gca()

    prev_num = 0

    for index, number in enumerate(bricks):
        print((index, number), (1, brick_size), number)

        if number == 1:
            facecolor='green'
        else:
            facecolor='red'

        prev_num += number

        renko = Rectangle((index, prev_num * brick_size), 1, brick_size, facecolor=facecolor, alpha=0.5)
        axes.add_patch(renko)

    plt.xlim([0, 2 * len(data)])
    plt.ylim([0, 2 * len(data)])
    plt.grid(True)

    major_ticks = np.arange(0, 2 * len(data), brick_size)
    minor_ticks = np.arange(0, 2 * len(data), 1)

    axes.set_xticks(major_ticks)
    axes.set_xticks(minor_ticks, minor=True)
    axes.set_yticks(major_ticks)
    axes.set_yticks(minor_ticks, minor=True)
    axes.grid(which='both')
    axes.grid(which='minor', alpha=0.2)
    axes.grid(which='major', alpha=0.5)

    plt.show()



data = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]
data = [1, 1, 1, -1, -1, 1, 1, 1, 1, 1]
plot_renko(data)

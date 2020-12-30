# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import time
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib

WIDTH = 100
HEIGHT = 100

matplotlib.use('TKagg')


def load_component(grid, i, j, filein):
    lines = open(filein, "r").read().split("\n")
    for line in lines:
        i2 = i
        for x in line:
            grid[j][i] = 0 if x == '.' else 1
            i += 1
        i = i2
        j += 1
    return grid


def next_generation(current_grid):
    new_grid = np.zeros((WIDTH, HEIGHT), dtype=int)
    for y in range(0, HEIGHT):
        y_before = y - 1 if y > 0 else HEIGHT - 1
        y_after = y + 1 if y < HEIGHT - 1 else 0
        for x in range(0, WIDTH):
            x_before = x - 1 if x > 0 else WIDTH - 1
            x_after = x + 1 if x < WIDTH - 1 else 0
            neighbor_sum = current_grid[y_before][x_before] + current_grid[y_before][x] + current_grid[y_before][
                x_after] + \
                           current_grid[y][x_before] + current_grid[y][x_after] + \
                           current_grid[y_after][x_before] + current_grid[y_after][x] + current_grid[y_after][x_after]
            if current_grid[y][x] == 0:
                if neighbor_sum == 3:
                    new_grid[y][x] = 1
            else:
                if neighbor_sum == 2 or neighbor_sum == 3:
                    new_grid[y][x] = 1
    return new_grid


def print_board(grid):
    pass
    # plt.clf()
    # plt.matshow(grid, 1)
    # plt.draw()
    # print()
    # for y in range(HEIGHT):
    #     print(''.join([". " if grid[y][x] == 0 else "O " for x in range(WIDTH)]))


def main():
    # plt.ion()
    # plt.show(block=False)
    start = int(round(time.time() * 1000))
    grid = np.zeros((WIDTH, HEIGHT), dtype=int)
    # grid = create_random_board((WIDTH, HEIGHT))
    grid = load_component(grid, 5, 3, "gosperglidergun.txt")
    for i in range(1000):
        # print_board(grid)
        # plt.pause(.0001)
        grid = next_generation(grid)
    end = int(round(time.time() * 1000))
    print(end - start)


def create_random_board(shape):
    rng = default_rng()
    return rng.integers(0, 2, shape[0] * shape[1]).reshape(shape)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

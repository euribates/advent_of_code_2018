#!/usr/bin/env python3

import argparse
from tools import CellMap

parser = argparse.ArgumentParser(description='Solution day 11, part 2')
parser.add_argument(
    '--test',
    dest='test',
    action='store_const',
    const=True,
    default=False,
)
parser.add_argument(
    '--serial',
    dest='serial',
    action='store',
    type=int,
    default=7347,
)


def main(options):
    grid = CellMap(options.serial)
    stats = []
    for size in range(1, 301):
        print(f'Size: {size}x{size}', flush=True)
        for y in range(1, 300-size):
            for x in range(1, 300-size):
                power = grid.powerNxN(x, y, size)
                stats.append((power, size, x, y))
    power, size, x, y = max(stats)
    print(power, size, x, y)
    print(f'Solution of part 2 in {x},{y},{size}')


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

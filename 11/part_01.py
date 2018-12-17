#!/usr/bin/env python3

import argparse
from tools import CellMap

parser = argparse.ArgumentParser(description='Solution day 11, part 1')
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
    for y in range(1, 299):
        for x in range(1, 299):
            power = grid.power3x3(x, y)
            stats.append((power, x, y))
    power, x, y = max(stats)
    print(power, x, y)
    print(f'Solution of part 1 in {x},{y}')


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

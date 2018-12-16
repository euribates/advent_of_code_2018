#!/usr/bin/env python3

from tools import read_input
from tools import get_names
from tools import Vector2
from tools import Scale
import collections
import argparse

parser = argparse.ArgumentParser(description='Analize puzzle')
parser.add_argument(
    '--test',
    dest='test',
    action='store_const',
    const=True,
    default=False,
)
parser.add_argument(
    '--steps',
    dest='steps',
    action='store',
    type=int,
    default=12000,
)


def find_area(dots):
    max_x = dots[max(dots, key=lambda k: dots[k].pos.x)].pos.x
    min_x = dots[min(dots, key=lambda k: dots[k].pos.x)].pos.x
    max_y = dots[max(dots, key=lambda k: dots[k].pos.y)].pos.y
    min_y = dots[min(dots, key=lambda k: dots[k].pos.y)].pos.y
    area = (max_x - min_x) * (max_y - min_y)
    return area


def tick(dots):
    for name in dots:
        d = dots[name]
        d.pos = d.pos + d.vel


def main(options):
    steps = options.steps
    if options.test:
        filename = 'sample.txt'
        output = 'sample.grafel'
    else:
        filename = 'input.txt'
        output = 'input.grafel'
    dots = collections.OrderedDict()
    for name, dot in zip(get_names(), read_input(filename)):
        dots[name] = dot
    stats = [(find_area(dots), 0)]
    for t in range(1, steps+1):
        tick(dots)
        area = find_area(dots)
        stats.append((area, t))
    min_stats = min(stats)
    print('Min area"', min_stats)
    print('Max area"', max(stats))
    solution = min_stats[1]
    print(f'Solution of part 2 in {solution}')


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

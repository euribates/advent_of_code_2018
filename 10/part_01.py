#!/usr/bin/env python3

from tools import read_input
from tools import get_names
from tools import Vector2
from tools import Scale
import collections
import argparse

parser = argparse.ArgumentParser(description='Solve puzzle')
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
    default=10,
)


def main(options):
    if options.test:
        filename = 'sample.txt'
        output = 'sample.grafel'
    else:
        filename = 'input.txt'
        output = 'input.grafel'
    dots = collections.OrderedDict()
    for name, dot in zip(get_names(), read_input(filename)):
        dots[name] = dot
    max_x = dots[max(dots, key=lambda k: dots[k].pos.x)].pos.x
    min_x = dots[min(dots, key=lambda k: dots[k].pos.x)].pos.x
    print('Range of x is [{} .. {}]'.format(min_x, max_x))
    max_y = dots[max(dots, key=lambda k: dots[k].pos.y)].pos.y
    min_y = dots[min(dots, key=lambda k: dots[k].pos.y)].pos.y
    print('Range of y is [{} .. {}]'.format(min_y, max_y))
    zoom = 512
    left_top = Vector2(min_x // zoom, min_y // zoom)
    right_bottom = Vector2(max_x // zoom, max_y // zoom)
    scale = Scale(left_top, right_bottom)
    print(f'Generating {output}', end=' ')
    with open(output, 'w') as fh:
        fh.write('Cast:\n\n')
        for name in dots:
            d = dots[name]
            x, y = scale(d.pos)
            x, y = d.pos
            print(f'    {name} = Circle pos {x}x{y} radius 1 color white', file=fh)
        fh.write('Actions:\n\n')
        for name in dots:
            dot = dots[name]
            x, y = scale(dot.pos) 
            print(f'    0-25 EaseIn {name} {x}x{y}', file=fh) 
        step_size = 2
        for frame in range(options.steps-100):
            for name in dots:
                dot = dots[name]
                dot.pos = dot.pos + dot.vel
        print('.', end='', flush=True)
        for frame in range(25):
            for name in dots:
                dot = dots[name]
                for _ in range(4):
                    dot.pos = dot.pos + dot.vel
                x, y = scale(dot.pos) 
                print(f'    {100+frame}-{100+frame+1} EaseIn {name} {x}x{y}', file=fh) 
        print('[OK]')


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

#!/usr/bin/env python3

import argparse
from tools import read_input
from tools import ImageMap
from tools import Cell
from tools import draw_frame

parser = argparse.ArgumentParser(description='Solution day 13, part 1')
parser.add_argument(
    '--test',
    dest='test',
    action='store_const',
    const=True,
    default=False,
)


def main(options):
    output = 'frames/frame_{:04d}.png'
    if options.test:
        filename = 'sample.txt'
    else:
        filename = 'input.txt'
    state = read_input(filename)
    frame = 0
    print(state)
    draw_frame(state, frame)
    while True:
        state.tick()
        frame += 1
        draw_frame(state, frame)
        if state.crashed:
            print('Found crash')
            print('crashed: {} {}'.format(state.crashed, type(state.crashed)))
            print(state)
            a, *b = list(state.crashed)
            solution = '{},{}'.format(a.x, a.y)
            print('Solution of part 1 is {}'.format(solution))
            break



if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

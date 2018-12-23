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
    filename = 'three_crosses_2.txt'
    state = read_input(filename)
    for frame in range(0, 150):
        print('--[Frame {}]-------------------'.format(frame))
        for car in state.get_cars():
            print(repr(car))
        draw_frame(state, frame)
        state.tick()


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

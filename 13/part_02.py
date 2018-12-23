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
    if options.test:
        filename = 'sample2.txt'
    else:
        filename = 'input.txt'
    state = read_input(filename)
    while True:
        state.tick()
        if state.crashed:
            print('Crashed: {}'.format(state.crashed))
            state.cars = [
                car 
                for car in state.cars
                if car not in state.crashed
                ]
            print('current num of cars: {}'.format(len(state.cars)))
        if len(state.cars) == 1:
            break
    print(state)
    print(state.cars)
    car = state.cars[0]
    solution = '{},{}'.format(car.x, car.y)
    print('Solution of parf 2 is {}'.format(solution))


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

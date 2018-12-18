#!/usr/bin/env python3


import argparse
from tools import read_input
from tools import State
from tools import Automat

parser = argparse.ArgumentParser(description='Solution day 11, part 1')
parser.add_argument(
    '--test',
    dest='test',
    action='store_const',
    const=True,
    default=False,
)


def main(options):
    if options.test:
        filename = 'sample.txt'
    else:
        filename = 'input.txt'
    initial_state, rules = read_input(filename)
    automat = Automat(initial_state, rules)
    print(automat.current_state)
    for i in range(5000000000):
        automat.evolve()
    solution = sum([
        k
        for k in automat.current_state.cells
        if automat.current_state.cells[k] == 1
        ])
    print(f'Solution of part 2 is {solution}')


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

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
    solution = sum([
        k
        for k in automat.current_state.cells
        if automat.current_state.cells[k] == 1
        ])
    for i in range(22):
        automat.evolve()
        print(automat.current_state)
        old_value = solution
        solution = sum([
            k
            for k in automat.current_state.cells
            if automat.current_state.cells[k] == 1
            ])
        # print(f'Step {i} solution in {solution} diff {solution-old_value}')
    
    def f(x):
        return 10617 + (x - 120)*69

    solution = f(50000000000-1)
    print(f'Solution of part 2 is {solution}')


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

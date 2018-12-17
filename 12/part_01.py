#!/usr/bin/env python3


import argparse
from tools import read_input
from tools import State

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
    buff = []
    current_state = initial_state
    for index, cells in current_state:
        print(index, cells, end=' ')
        for rule in rules:
            applied, result = rule.produce(cells)
            if applied:
                buff.append(result)
                print('rule {} match'.format(rule), end='')
                break
        else:
            buff.append('.')
            print('default rule', end='')
        print()
    print()
    print(initial_state)
    print(''.join(buff))

    current_state = State(''.join(buff))
    buff = []
    for index, cells in current_state:
        for rule in rules:
            applied, result = rule.produce(cells)
            if applied:
                buff.append(result)
                break
        else:
            buff.append('.')
    print(''.join(buff))


if __name__ == '__main__':
    options = parser.parse_args()
    main(options)

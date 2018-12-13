#!/usr/bin/env python3

from tools import read_input, create_tree

root = create_tree(read_input('input.txt'))

solution = root.value()
print('Solution of part 2 in {}'.format(solution))

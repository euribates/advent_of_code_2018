#!/usr/bin/env python3

from tools import read_input, create_tree

root = create_tree(read_input('input.txt'))

def sum_metadata(node, acc=0):
    for son in node.sons:
        acc += sum_metadata(son)
    acc += sum(node.metadata)
    return acc

solution = sum_metadata(root)
print('Solution of part 1 in {}'.format(solution))

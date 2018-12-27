#!/usr/bin/env python3

from tools import Recipes
from tools import is_sublist

def find_seq(sample):
    target = [int(c) for c in sample]
    r = Recipes()
    index = is_sublist(target, list(r.last_items))
    while index is -1:
        r.next()
        index = is_sublist(target, list(r.last_items))
    # print('r', r)
    # print('r.size', r.size)
    # print('text:', text)
    return r.size - len(r.last_items) + index

assert find_seq('51589') == 9
assert find_seq('92510') == 18
assert find_seq('59414') == 2018
assert find_seq('01245') == 5

solution = find_seq('681901')
print('Solution of part 2 is {}'.format(solution))


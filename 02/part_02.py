#!/usr/bin/env python3

from collections import Counter
from functools import partial
from itertools import permutations


def read_input(filename='input.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return (line.strip() for line in lines)


def find_one_diff(seq_a, seq_b):
    bit_match = [
        a == b
        for a,b in zip(seq_a, seq_b)
        ]
    if sum([0 if bit else 1 for bit in bit_match]) == 1:
        return True, bit_match.index(False)
    return False, -1


if __name__ == '__main__':
    box_ids = read_input()
    for a, b in permutations(box_ids, 2):
        flag, index = find_one_diff(a, b)
        if flag:
            solution = a[:index] + a[index+1:]
            print(f"key a: {a}")
            print(f"key b: {b}")
            print(f"Solution of part 2: {solution}")
            break

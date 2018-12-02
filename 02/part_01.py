#!/usr/bin/env python3

from collections import Counter
from functools import partial


def read_input(filename='input.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return (line.strip() for line in lines)


def count_for(seq, num=0):
    c = Counter(seq)
    return 1 if any([
        t[1] == num for t in c.items()
        ]) else 0


if __name__ == '__main__':
    count_for_two = partial(count_for, num=2)
    count_for_three = partial(count_for, num=3)
    acc_two = acc_three = 0
    for box_id in read_input():
        acc_two += count_for_two(box_id)
        acc_three += count_for_three(box_id)
    solution = acc_two * acc_three
    print(f"Solution of part 1: {solution}")

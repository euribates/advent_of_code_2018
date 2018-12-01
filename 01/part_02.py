#!/usr/bin/env python3

from itertools import cycle

with open('input.txt', 'r') as f:
    lines = f.readlines()
nums = [int(_.strip()) for _ in lines]


def find_freq(seq, tron=False):
    acc = 0
    seen_numbers = set([0])
    for num in cycle(seq):
        acc += num
        if tron:
            print(f"acc: {acc} num: {num} seen_numbers: {seen_numbers}")
        if acc in seen_numbers:
            return acc
        seen_numbers.add(acc)

solution = find_freq(nums)
print(f'Solution for part 2: {solution}')

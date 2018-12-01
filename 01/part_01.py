#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = f.readlines()

nums = [int(_.strip()) for _ in lines]
solution = sum(nums)
print(f'Solution of part 1: {solution}')

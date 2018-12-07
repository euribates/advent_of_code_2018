#!/usr/bin/env python3

import tools

if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        data = fh.read().strip()
        dl = tools.DL(data)
    dl.reduce()
    solution = len(dl)
    print(f'Solution of part 1: {solution}')

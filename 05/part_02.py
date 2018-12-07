#!/usr/bin/env python3

import collections
import tools

if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        data = fh.read().strip()
    stats = collections.OrderedDict()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(f'Analyzing {letter}', end=' ', flush=True)
        subdata = data.replace(letter, '')
        subdata = subdata.replace(letter.upper(), '')
        dl = tools.DL(subdata)
        dl.reduce()
        stats[letter] = len(dl)
        print(f'[OK] (size is {len(dl)})', flush=True)
    letter = min(stats, key=lambda k: stats[k])
    solution = stats[letter]
    print(f'Solution of part 2 (letter is {letter}): {solution}')

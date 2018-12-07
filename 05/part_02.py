#!/usr/bin/env python3

import sys

import collections
import tools

if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        data = fh.read().strip()
    stats = collections.OrderedDict()
    minimo = len(data)
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(f'Analyze {letter}', end=' ')
        sys.stdout.flush()
        subdata = data.replace(letter, '')
        subdata = subdata.replace(letter.upper(), '')
        dl = tools.DL(subdata)
        dl.reduce()
        stats[letter] = len(dl)
        if len(dl) < minimo:
            min_letter = letter
            minimo = len(dl)
        print('[OK]')
        sys.stdout.flush()

    print(stats)
    solution = min_letter
    print(f'Solution ofxpart 1: {solution}')

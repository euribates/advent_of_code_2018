#!/usr/bin/env python3

import tools

if __name__ == "__main__":
    with open('input.txt', 'r') as fh:
        data = fh.read().strip()
        dl = tools.DL(data)
    num_loops = 0
    while True:
        num_loops += 1
        if num_loops % 1000 == 0:
            print('progress {:.2f}%'.format(len(dl)*100./len(data)))
        for n in dl:
            num_changes = dl.react(n)
            if num_changes > 0:
                break
        if num_changes == 0:
            break
    solution = len(dl)
    print(f'Solution of part 1: {solution}')

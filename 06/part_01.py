#!/usr/bin/env python3

import tools


if __name__ == '__main__':
    m = tools.ColorMap('input.txt')
    m.analyze()
    options = set([name for name in m.kernel])
    print('N. options is {}'.format(len(options)))
    for x in range(m.min_x, m.max_x+1):
        color = m.plane[(x, m.min_y)]
        options.discard(color)
        color = m.plane[(x, m.max_y)]
        options.discard(color)
    for y in range(m.min_y, m.max_y+1):
        color = m.plane[(m.min_x, y)]
        options.discard(color)
        color = m.plane[(m.max_x, y)]
        options.discard(color)
    print('N. options is {}'.format(len(options)))
    solutions = [(name, m.size[name]) for name in options]
    solution = max(solutions, key=lambda t: t[1])
    print(solution)

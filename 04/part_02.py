#!/usr/bin/env python

import tools
import collections

if __name__ == '__main__':
    by_date = collections.defaultdict(list)
    for (code, day, hhmm, msg, guard_id) in tools.read_input():
        by_date[day].append((code, hhmm, guard_id))
    kernel = collections.OrderedDict()
    for day in by_date:
        m = tools.Mapa(day)
        for (code, hhmm, guard_id) in by_date[day]:
            m.add(code, hhmm, guard_id)
        kernel[day] = m
    matrix = collections.defaultdict(int)
    for k in kernel:
        m = kernel[k]
        id_guard = m.guard_id
        bar = m.bar
        for minute in range(60):
            matrix[(minute, id_guard)] += 1 if bar[minute] == '#' else 0
    print(matrix)
    sorted_list = sorted([
        (num, minute, id_guard) for ((minute, id_guard), num) in matrix.items()
        ], reverse=True)
    for num, minute, guard in sorted_list[0:10]:
        print(num, minute, guard)
    (num, minute, guard) = sorted_list[0]   
    solution = minute * guard
    print(f'Solution part 2 is {solution}')

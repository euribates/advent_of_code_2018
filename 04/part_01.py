#!/usr/bin/env python

import tools
import collections

if __name__ == '__main__':
    by_date = collections.defaultdict(list)
    for (code, day, hhmm, msg, guard_id) in tools.read_input():
        by_date[day].append((code, hhmm, guard_id))
        print(code)

    print(
        ' '*12,
        '000000000011111111112222222222333333333344444444445555555555'
        )
    print(
        ' '*12,
        '012345678901234567890123456789012345678901234567890123456789'
        )
    max_sleep = 0
    max_sleep_safe = 0
    max_day = None
    max_guard_id = None
    stat_guards = collections.defaultdict(int)
    buff = []
    for day in by_date:
        m = tools.Mapa(day)
        for (code, hhmm, guard_id) in by_date[day]:
            m.add(code, hhmm, guard_id)
        print(m)
        if m.guard_id == 727:
            buff.append(m.bar)
        if m.sleep_time() > max_sleep:
            max_sleep = m.sleep_time()
            max_day = m.day
            max_guard_id = m.guard_id
        max_sleep_safe = max(max_sleep_safe, m.sleep_time())
        stat_guards[m.guard_id] += m.sleep_time()

    print('max sleep safe: {}'.format(max_sleep_safe))
    print('max sleep: {}'.format(max_sleep))
    print('day: {}'.format(max_day))
    print('guard id: {}'.format(max_guard_id))
    print('Stats')
    id_guard = None
    minutes = -1
    for k in stat_guards:
        m = stat_guards[k]
        if m > minutes:
            id_guard = k
            minutes = m
        print('Guard {} sleep {} minutes'.format(k, stat_guards[k]))

    print('Found guard: {}'.format(id_guard))
    cols = [0] * 60
    for i in range(60):
        cols[i] = sum([1 if line[i] == '#' else 0 for line in buff])
    print(cols)
    m = max(cols)
    minute = cols.index(m)
    print('Minute is {}'.format(minute))

    solution = id_guard * minute
    print(f'Part 1 solution: {solution}')

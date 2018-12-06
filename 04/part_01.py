#!/usr/bin/env python

import tools
import collections

from constants import BEGIN_SHIFT, WAKE_UP, FALL_SLEEP


class Mapa:

    def __init__(self, day):
        self.day = day
        self.slots = ['.'] * 60
        self.top = 0
        self.guard_id = -1

    def add(self, code, hhmm, guard_id):
        hh, mm = int(hhmm[:2]), int(hhmm[-2:])
        if (code == BEGIN_SHIFT and hh == 0) or self.guard_id == -1:
            self.guard_id = guard_id
            if hh == 0:
                self.top = mm
        elif code == FALL_SLEEP:
            # print('FALL SLEEP {}'.format(mm))
            self.top = mm 
        elif code == WAKE_UP:
            # print('WAKE UP {}'.format(mm))
            for index in range(self.top, mm):
                self.slots[index] = '#'
            self.top += mm

    @property
    def bar(self):
        return ''.join(self.slots)

    def sleep_time(self):
        return self.bar.count('#')

    def __str__(self):
        return '{} #{:<5} {}'.format( self.day, self.guard_id, self.bar)



if __name__ == '__main__':
    i = 0
    by_date = collections.defaultdict(list)
    for (code, day, hhmm, msg, guard_id) in tools.read_input():
        by_date[day].append((code, hhmm, guard_id))
        print(code)

print(' '*12, '000000000011111111112222222222333333333344444444445555555555')
print(' '*12, '012345678901234567890123456789012345678901234567890123456789')
max_sleep = 0
max_sleep_safe = 0
max_day = None
max_guard_id = None
stat_guards = collections.defaultdict(int)
buff = []
for day in by_date:
    m = Mapa(day)
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
for k in stat_guards:
    print('Guard {} sleep {} minutes'.format(k, stat_guards[k]))

for l in buff:
    print(l)

cols = [0] * 60
for i in range(60):
    cols[i] = sum([1 if line[i] == '#' else 0 for line in buff])
print(cols)
m  = max(cols)
minuto = cols.index(m)
print(minuto)

solution = 727 * minuto
print(f'Part 1 solution: {solution}')

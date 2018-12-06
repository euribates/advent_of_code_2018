#!/usr/bin/env python3

from parse import parse
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
        return '{} #{:<5} {}'.format(self.day, self.guard_id, self.bar)


def read_input(filename='input.txt'):
    guard_id = None
    with open(filename, 'r') as f:
        for line in sorted(f):
            day = line[6:11]
            hhmm = line[12:17]
            msg = line[19:].strip()
            mg = parse("Guard #{:d} begins shift", msg)
            ms = parse("falls asleep", msg)
            mw = parse("wakes up", msg)
            if mg:
                guard_id = int(mg[0])
                yield BEGIN_SHIFT, day, hhmm, msg, guard_id
            elif ms:
                yield FALL_SLEEP, day, hhmm, msg, guard_id
            elif mw:
                yield WAKE_UP, day, hhmm, msg, guard_id

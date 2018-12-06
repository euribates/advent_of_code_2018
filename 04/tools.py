#!/usr/bin/env python3

from parse import parse
from constants import BEGIN_SHIFT, WAKE_UP, FALL_SLEEP




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

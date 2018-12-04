#!/usr/bin/env python3

import re
from parse import parse


def identity(x):
    return x


def read_input(filename='input.txt', transform=identity):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return (transform(line.strip()) for line in lines)


def parse_log(s):
    ts = s[1:17]
    msg = s[19:]
    guard_id = None
    if msg.startswith('Guard'):
        m = parse("Guard #{:d} begins shift", msg)
        guard_id = m[0]
    return ts, msg, guard_id

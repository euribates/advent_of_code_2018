#!/usr/bin/env python3

import re
import itertools

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY'
nums = '0123456789'
alphanums = alpha + nums


def get_names(first=alpha, rest=alphanums):
    for a, b in itertools.product(first, rest):
        yield '{}{}'.format(a, b)


class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return '<{}, {}>'.format(self.x, self.y)

    def __repr__(self):
        return 'Vector2({}, {})'.format(self.x, self.y)


class Dot:

    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def __repr__(self):
        return 'Dot({}, {})'.format(
            self.pos,
            self.vel,
            )


pat_line = re.compile('position=<(.+)> velocity=<(.+)>')


def read_input(filename='input.txt', pattern=pat_line):
    with open(filename, 'r') as fh:
        for line in fh:
            m = pattern.match(line.strip())
            pos = Vector2(*[int(v.strip()) for v in m.group(1).split(',')])
            vel = Vector2(*[int(v.strip()) for v in m.group(2).split(',')])
            yield Dot(pos, vel)


class Scale:

    def __init__(self, left_top, right_bottom, width=640, height=400):
        x0 = left_top.x
        y0 = left_top.y
        x1 = right_bottom.x
        y1 = right_bottom.y
        local_width = float(x1 - x0)
        self.x_factor = float(width) / local_width
        self.x_offset = -x0 * self.x_factor
        local_height = float(y1 - y0)
        self.y_factor = float(height) / local_height
        self.y_offset = -y0 * self.y_factor

    def __call__(self, p):
        x, y = p.x, p.y
        return Vector2(
            int(round(self.x_factor * x + self.x_offset)),
            int(round(self.y_factor * y + self.y_offset)),
            )

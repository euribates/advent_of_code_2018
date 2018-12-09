#!/usr/bin/env python3

import re
import random
import collections


names = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_names():
    global names
    for letter in names:
        yield letter


def parse(line, names=get_names(), pat_coords=re.compile(r'(\d+), (\d+)')):
    m = pat_coords.match(line)
    x, y = int(m.group(1)), int(m.group(2))
    return next(names), x, y


def read_input(filename='input.txt', transform=parse):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return (transform(line.strip()) for line in lines)


def distance(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return abs(x0 - x1) + abs(y0 - y1)


def get_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        )


class ColorMap:

    def __init__(self, filename='input.txt'):
        self.plane = {}
        self.kernel = collections.OrderedDict()
        self.color = {}
        self.size = collections.defaultdict(int)
        self.X = []
        self.Y = []
        self.load(filename)

    def __getitem__(self, name):
        return self.kernel[name]

    def load(self, filename):
        for name, x, y in read_input(filename):
            self.kernel[name] = (x, y)
            self.X.append(x)
            self.Y.append(y)
            self.color[name] = get_color()
            self.plane[(x, y)] = name
        self.min_x = min(self.X)
        self.max_x = max(self.X)
        self.min_y = min(self.Y)
        self.max_y = max(self.Y)

    def find_nearest(self, x, y):
        p0 = (x, y)
        d = sorted([
            (distance(p0, self.kernel[k]), k)
            for k in self.kernel
            ])
        d0, name0 = d[0]
        d1, name1 = d[1]
        return '0' if d0 == d1 else name0

    def analyze(self):
        for x in range(0, self.max_x+1):
            for y in range(0, self.max_y+1):
                if (x, y) in self.kernel:
                    continue
                name = self.find_nearest(x, y)
                self.plane[(x, y)] = name
                self.size[name] += 1

#!/usr/bin/env python3

import re


def identity(x):
    return x


def read_input(filename='input.txt', transform=identity):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return (transform(line.strip()) for line in lines)


class Claim:

    pat = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

    def __init__(self, s):
        m = Claim.pat.match(s)
        if not m:
            raise ValueError("Wrong clain format: {}".format(s))
        self.id = int(m.group(1))
        self.left = int(m.group(2))
        self.top = int(m.group(3))
        self.width = int(m.group(4))
        self.height = int(m.group(5))

    def __repr__(self):
        return "Claim('#{} @ {},{}: {}x{}')".format(
            self.id,
            self.left,
            self.top,
            self.width,
            self.height,
            )

    def __iter__(self):
        self.x = self.left
        self.y = self.top
        for w in range(self.width):
            for h in range(self.height):
                yield (self.x + w, self.y + h)


def parse(line):
    return Claim(line)


def print_mapa(mapa, cols=10, rows=10):
    print()
    for row in range(rows):
        for col in range(cols):
            v = mapa[(row, col)]
            print(v if v > 0 else '.', end='')
        print()

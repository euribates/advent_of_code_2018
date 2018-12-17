#!/usr/bin/env python

import numpy as np


class Cell:

    def __init__(self, serial):
        self.serial = serial

    def __call__(self, x, y):
        rank = x + 10
        power_level = rank * y
        power_level += self.serial
        power_level *= rank
        s = str(power_level)
        result = int(s[-3]) if len(s) >= 3 else 0
        return result - 5


class CellMap:

    def __init__(self, serial, rows=300, cols=300):
        self.cell = Cell(serial)
        self.kernel = np.zeros((rows+2, cols+2))
        for y in range(1, rows+1):
            for x in range(1, cols+1):
                self.kernel[x, y] = self.cell(x, y)

    def power(self, x, y):
        return self.kernel[x, y]

    def power3x3(self, x, y):
        x0, x1 = x, x+3
        y0, y1 = y, y+3
        return self.kernel[x0:x1, y0:y1].sum()

    def powerNxN(self, x, y, size):
        if size == 1:
            return self.kernel[x, y]
        else:
            x0, x1 = x, x+size
            y0, y1 = y, y+size
            return self.kernel[x0:x1, y0:y1].sum()

#!/usr/bin/env python3

import pytest

from tools import Cell


class Sample:

    def __init__(self, serial, x, y, target):
        self.serial = serial
        self.x = x
        self.y = y
        self.target = target

    def __str__(self):
        return f'Cell at {self.x}x{self.y}, '  \
               f'grid serial number {self.serial}:'  \
               f'power level is {self.target}'


samples = [
    Sample(8, 3, 5, 4),    
    Sample(57, 122,79, -5),
    Sample(39, 217, 196, 0),
    Sample(71, 101, 153, 4),  
    ]


@pytest.fixture(params=samples, ids=str)
def sample(request):
    return request.param

def test_cell(sample):
    cell = Cell(sample.serial)
    assert cell(sample.x, sample.y) == sample.target
    
